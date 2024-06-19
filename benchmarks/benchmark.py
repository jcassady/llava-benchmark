class Benchmark:
    """
    A general-purpose class for processing benchmark results.

    Attributes:
        method (function): A function to process benchmark results.
    """

    def __init__(self, method):
        """
        Initializes a new instance of the Benchmark class.

        Args:
            method (function): A function to process benchmark results.
        """
        self.method = method

    def process(self, benchmark_result):
        """
        Processes a benchmark result using the function stored in self.method.

        Args:
            benchmark_result: The benchmark result to process.

        Returns:
            The result of calling self.method with benchmark_result.
        """
        return self.method(benchmark_result)
