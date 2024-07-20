"""
This module provides benchmarks for processing Ollama's evaluation rate data.

It contains the EvalRateBenchmark class, which includes methods for
calculating, processing, and storing evaluation rates measured in
tokens per second.
"""


# Local library imports.
from .eval_rate_processor import EvalRateProcessor
from .eval_rate_plotter import EvalRatePlotter


class EvalRateBenchmark():
    def __init__(self):
        self.current_eval_rate = None
        self.eval_rates = []
        self.image_file_paths = []

        self.eval_rate_plotter = EvalRatePlotter()

    def average_rate(self):
        """
        Calculates the average of the evaluation rates stored in the instance.
        Interface to EvalRateProcessor's average_eval_rates method from the
        LlavaBenchmark class.

        Returns:
            float: The average evaluation rate.
        """
        return EvalRateProcessor.average_eval_rates(self.eval_rates)

    def process_eval_rate(self, benchmark_result):
        self.current_eval_rate = EvalRateProcessor.process_eval_rate(
            benchmark_result)

    def store_eval_rate(self, image_file_path: str):
        if self.current_eval_rate is not None:
            self.eval_rates.extend(self.current_eval_rate)
            self.image_file_paths.append(image_file_path)
