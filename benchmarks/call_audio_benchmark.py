# Standard Library imports.
import os
import re
import textwrap

'''
Whisper is an advanced natural language processing (NLP) library
developed by OpenAI. Class CallAudioBenchmark utilizes whisper
to transcribe call audio files to text transcripts, before handing
them off to a LLaVA model for summarization as call notes.
'''
import whisper


class CallAudioBenchmark():
    """
    A class for processing call audio and extracting call notes.

    Args:
        model (str, optional): The name of the Whisper ASR model to use. Defaults to "base".

    Attributes:
        current_transcript (str): The most recent transcript obtained from audio processing.
        transcripts (list): A list of all transcripts processed.
        model_transcripts (dict): A dictionary mapping LLAVA models to their respective transcripts.
        call_notes (str): Extracted call notes from benchmark results.
        model_call_notes (dict): A dictionary mapping LLAVA models to their call notes.
        model (whisper.WhisperModel): The Whisper ASR model instance.

    Methods:
        media_file_path(media_file: str) -> str:
            Returns the absolute path to the specified media file.

        process_audio(audio_file: str) -> whisper.Audio:
            Loads and processes the audio file, returning the padded or trimmed audio.

        transcribe_audio(call_audio: whisper.Audio) -> str:
            Transcribes the audio using the Whisper model and returns the transcript.

        store_transcript(llava_model: str, fp16: bool = False) -> None:
            Stores the current transcript along with the LLAVA model it corresponds to.

        store_call_notes(llava_model: str, benchmark_result: str) -> None:
            Extracts and stores call notes from benchmark results.

        print_call_notes() -> None:
            Prints formatted call notes.

    Note:
        This class assumes the existence of the Whisper ASR model and audio data.
    """

    def __init__(self, model: str = "base"):
        # Transcript instance variables. 
        self.current_transcript = None
        self.transcripts = []
        self.model_transcripts = {}

        # Call notes instance variables.
        self.call_notes = None
        self.model_call_notes = {}
        self.model = whisper.load_model(model)

    def media_file_path(self, media_file: str):
        """
        Returns the absolute path to the specified call audio file.

        Args:
            media_file (str): The name of the call audio file.

        Returns:
            str: The absolute call audio file path.
        """
        return os.path.abspath("data\\" + "call_audio\\" + media_file)

    def process_audio(self, audio_file: str):
        """
        Loads and processes the audio file, returning the padded or trimmed audio.

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
        Transcribes the audio using the Whisper model and returns the transcript.

        Args:
            call_audio (whisper.Audio): Processed audio data.

        Returns:
            str: The transcribed text.
        """
        self.current_transcript = self.model.transcribe(
            call_audio, fp16=False)["text"]
        return self.current_transcript

    def store_transcript(self, llava_model: str, fp16: bool = False) -> None:
        """
        Stores the current transcript along with the LLAVA model it corresponds to.

        Args:
            llava_model (str): The LLAVA model name.
            fp16 (bool, optional): Whether FP16 mode is enabled. Defaults to False.
        """
        if self.current_transcript is not None:
            self.transcripts.append(self.current_transcript)
            self.model_transcripts[llava_model] = self.current_transcript

    def store_call_notes(self, llava_model: str, benchmark_result: str):
        """
        Extracts and stores call notes from benchmark results.

        Args:
            llava_model (str): The LLAVA model name.
            benchmark_result (str): The benchmark result output.
        """
        pattern = re.compile(
            r'failed to get console mode for stderr: The handle is invalid\.(.*)', re.DOTALL)
        match = pattern.search(benchmark_result.stdout)

        if match:
            self.call_notes = match.group(1)
            self.model_call_notes[llava_model] = self.call_notes.strip()
        else:
            self.model_call_notes[llava_model] = None

    def print_call_notes(self):
        """
        Prints formatted call notes.

        Note:
            The call notes are wrapped to a maximum width of 40 characters using textwrap.
        """
        separator = '-' * 40
        section_title = "\ncall notes:".upper()
        lines = self.call_notes.strip().splitlines()
        wrapped_lines = [textwrap.fill(
            line, width=40, initial_indent="| ", subsequent_indent="| ") for line in lines]

        print(separator)
        print(section_title)
        for wrapped_line in wrapped_lines:
            print(wrapped_line)
        print("\n")
