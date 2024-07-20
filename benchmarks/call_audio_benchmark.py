"""
call_audio_benchmark.py module.

This module contains the CallAudioBenchmark class for processing
audio and extracting call notes by leveraging both Whisper and
LLaVA models.

Whisper is an advanced natural language processing (NLP) library
developed by OpenAI. Class CallAudioBenchmark utilizes whisper
to transcribe call audio files to text transcripts, before handing
them off to a LLaVA model for summarization as call notes.
"""

# Standard library imports.
import os
import re

# Third-party imports.
import whisper

# Set max width for printed call notes.
MAX_WIDTH = 40


class CallAudioBenchmark:
    """
    A class for processing call audio and extracting call notes.

    Args:
        model (str, optional): The name of the Whisper ASR model to use.
        Defaults to "base".

    Attributes:
        current_transcript (str): The most recent transcript obtained from
        audio processing.
        transcripts (list): A list of all transcripts processed.
        model_transcripts (dict): A dictionary mapping LLAVA models to their
        respective transcripts.
        call_notes (str): Extracted call notes from benchmark results.
        model_call_notes (dict): A dictionary mapping LLAVA models to their
        call notes.
        model (whisper.WhisperModel): The Whisper ASR model instance.

    Methods:
        media_file_path(media_file: str) -> str:
            Returns the absolute path to the specified media file.

        process_audio(audio_file: str) -> whisper.Audio:
            Loads and processes the audio file, returning the padded or
            trimmed audio.

        transcribe_audio(call_audio: whisper.Audio) -> str:
            Transcribes the audio using the Whisper model and returns the
            transcript.

        store_transcript(llava_model: str, fp16: bool = False) -> None:
            Stores the current transcript along with the LLAVA model it
            corresponds to.

        store_call_notes(llava_model: str, benchmark_result: str) -> None:
            Extracts and stores call notes from benchmark results.

        print_call_notes() -> None:
            Prints formatted call notes.

    Note:
        This class assumes the existence of the Whisper ASR model and
        audio data.
    """

    def __init__(self, model: str = 'base'):
        """
        Initialize a new instance of CallAudioBenchmark.

        Args:
            model (str): The name of the Whisper model to load.
                Default is "base".
        """
        # Transcript instance variables.
        self.current_transcript = None
        self.transcripts = []
        self.model_transcripts = {}

        # Call notes instance variables.
        self.call_notes = None
        self.model_call_notes = {}

    def media_file_path(self, media_file: str) -> str:
        """
        Return the absolute path to the specified call audio file.

        Args:
            media_file (str): The name of the call audio file.

        Returns:
            str: The absolute call audio file path.
        """
        base_dir = 'data'
        call_audio_dir = 'call_audio'
        return os.path.abspath(
            os.path.join(base_dir, call_audio_dir, media_file),
        )

    def process_audio(self, audio_file: str):
        """
        Load and process the audio file, trimmed Whisper audio data.

        Args:
            audio_file (str): The name of the audio file.

        Returns:
            whisper.Audio: Processed audio data.
        """
        audio_file_path = self.media_file_path(audio_file)
        call_audio = whisper.load_audio(audio_file_path)
        return whisper.pad_or_trim(call_audio)

    def transcribe_audio(self, call_audio: whisper.audio):
        """
        Transcribe the audio using Whisper and return the transcript.

        Args:
            call_audio (whisper.Audio): Processed audio data.

        Returns:
            str: The transcribed text.
        """
        self.current_transcript = self.model.transcribe(
            call_audio,
            fp16=False,
        )['text']
        return self.current_transcript

    def store_transcript(self, llava_model: str, fp16: bool = False) -> None:
        """
        Store the current transcript along with the LLAVA model name.

        Args:
            llava_model (str): The LLAVA model name.
            fp16 (bool): Whether FP16 mode is enabled. Defaults to False.
        """
        if self.current_transcript is not None:
            self.transcripts.append(self.current_transcript)
            self.model_transcripts[llava_model] = self.current_transcript

    def store_call_notes(self, llava_model: str, benchmark_result: str):
        """
        Extract and store call notes from benchmark results.

        Args:
            llava_model (str): The LLAVA model name.
            benchmark_result (str): The benchmark result output.
        """
        pattern = re.compile(
            r'The stderr handle is invalid\.(.*)',
            re.DOTALL,
        )
        match = pattern.search(benchmark_result.stdout)

        if match:
            self.call_notes = match.group(1)
            self.model_call_notes[llava_model] = self.call_notes.strip()
        else:
            self.model_call_notes[llava_model] = None

    def print_call_notes(self):
        """Print formatted call notes."""
        lines = self.call_notes.strip().splitlines()
        wrapped_lines = [
            f'| {line}' if i == 0 else f'| {line}'
            for i, line in enumerate(lines)
        ]

        print('-' * MAX_WIDTH)
        print('\ncall notes:'.upper())
        for wrapped_line in wrapped_lines:
            print(wrapped_line)
        print('\n')

