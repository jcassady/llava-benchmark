# Standard library imports.
import re

# Local library imports.
from .eval_rate_processor import EvalRateProcessor
from .eval_rate_plotter import EvalRatePlotter
from benchmarks.benchmark import Benchmark


class EvalRateBenchmark(Benchmark):
    """
    A benchmark class for evaluating the rate of a model.
    This class inherits from the Benchmark class.
    """

    def __init__(self):
        """
        Initializes the EvalRateBenchmark instance and sets up the process method.
        The process method is set to the process_eval_rate method of an
        EvalRateProcessor instance.
        """
        super().__init__(EvalRateProcessor().process_eval_rate)
        self.eval_rate_plotter = EvalRatePlotter()

        self.eval_rates = []
        self.image_file_paths = []

    def average_rate(self):
        """
        Calculates the average of the evaluation rates stored in the instance.

        Returns:
            float: The average evaluation rate.
        """
        return EvalRateProcessor().average_eval_rates(self.eval_rates)

    def store_eval_rate(self, benchmark_result, image_file_path):
        """
        Stores the evaluation rate from the benchmark result in the instance.

        Args:
            benchmark_result: The result of the benchmark.
            image_file_path (str): File path of the image.

        Returns:
            The evaluation rate.
        """
        result = super().process(benchmark_result)
        if result is not None:
            self.eval_rates.extend(result)
            self.image_file_paths.append(image_file_path)
        return result
