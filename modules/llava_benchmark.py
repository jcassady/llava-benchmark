from benchmarks.eval_rate_benchmark import EvalRateBenchmark
from benchmarks.license_plate_benchmark import LicensePlateBenchmark

class LlavaBenchmark:
    """
    A class to handle benchmarks for LLaVA models.

    ...

    Attributes
    ----------
    benchmarks : list
        a list of benchmarks

    Methods
    -------
    store_results(benchmark_result, model, image_file_path):
        Stores the benchmark results.
    average_and_plot_benchmarks():
        Calculates the average evaluation rates and plots them.
    """

    def __init__(self, benchmarks):
        """
        Constructs all the necessary attributes for the LlavaBenchmark object.

        Parameters
        ----------
            benchmarks : list
                a list of benchmarks
        """
        self.benchmarks = benchmarks

    def store_results(self, benchmark_result, model, image_file_path):
        """
        Stores the benchmark results.

        Parameters
        ----------
        benchmark_result : CompletedProcess
            The result of the subprocess.run call.
        model : str
            The name of the model to use.
        image_file_path : str
            The image file path.
        """
        for benchmark in self.benchmarks:
            if isinstance(benchmark, EvalRateBenchmark):
                # Store the eval rate result from each benchmark.
                benchmark.store_eval_rate(
                    benchmark_result, image_file_path)
            elif isinstance(benchmark, LicensePlateBenchmark):
                # Store the license plate number from each benchmark.
                benchmark.store_license_plate(model, benchmark_result)

    def average_and_plot_benchmarks(self):
        """
        Calculates the average evaluation rates and plots them.
        """
        for benchmark in self.benchmarks:
            if isinstance(benchmark, EvalRateBenchmark):
                # Calculate the mean evaluation rate.
                benchmark.average_rate()
                # Visualize evaluation rates with a plot.
                benchmark.eval_rate_plotter.plot(benchmark.eval_rates)
