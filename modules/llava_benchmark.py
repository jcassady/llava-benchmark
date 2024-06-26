# Standard library imports.
from typing import List

# Local library imports.
from benchmarks.eval_rate_benchmark import EvalRateBenchmark
from benchmarks.license_plate_benchmark import LicensePlateBenchmark
from benchmarks.call_audio_benchmark import CallAudioBenchmark



class LlavaBenchmark:
    """
    LLaVA Benchmark class for processing media and storing results.

    Attributes:
        benchmarks (list): List of benchmark instances.
    """

    def __init__(self, benchmarks: List):
        """
        Initialize LlavaBenchmark instance.

        Args:
            benchmarks (list): List of benchmark instances.
        """
        self.benchmarks = benchmarks

    def process_media(self, media_file: str) -> tuple:
        """
        Process media file and return relevant information.

        Args:
            media_file (str): Path to the media file.

        Returns:
            tuple: A tuple containing transcript (str) and media file path (str).
        """
        for benchmark in self.benchmarks:
            if isinstance(benchmark, EvalRateBenchmark):
                pass  # No media to process for EvalRateBenchmark.
            elif isinstance(benchmark, LicensePlateBenchmark):
                _transcript = ""  # Dummy transcript object.
                media_file_path = benchmark.media_file_path(media_file)
                return _transcript, media_file_path
            elif isinstance(benchmark, CallAudioBenchmark):
                processed_audio = benchmark.process_audio(media_file)
                transcript = benchmark.transcribe_audio(processed_audio)
                media_file_path = benchmark.media_file_path(media_file)
                return transcript, media_file_path

    def store_results(self, benchmark_result: str, model: str, media_file_path: str) -> None:
        """
        Store the benchmark results.

        Args:
            benchmark_result (subprocess.CompletedProcess): Result of the subprocess.run call.
            model (str): The name of the model to use.
            media_file_path (str): The media file path.
        """
        for benchmark in self.benchmarks:
            if isinstance(benchmark, EvalRateBenchmark):
                benchmark.process_eval_rate(benchmark_result)
                benchmark.store_eval_rate(media_file_path)
            elif isinstance(benchmark, LicensePlateBenchmark):
                benchmark.store_license_plate(model, benchmark_result)
            elif isinstance(benchmark, CallAudioBenchmark):
                benchmark.store_transcript(model)
                benchmark.store_call_notes(model, benchmark_result)
                benchmark.print_call_notes()

    def average_and_plot_benchmarks(self) -> None:
        """
        Calculate the average evaluation rates and plot them.
        """
        for benchmark in self.benchmarks:
            if isinstance(benchmark, EvalRateBenchmark):
                benchmark.average_rate()
                benchmark.eval_rate_plotter.plot(benchmark.eval_rates)
