# Standard library imports.
import re


class EvalRateProcessor:
    """
    A class used to process the evaluation rate from benchmark results.

    ...

    Methods
    -------
    process_eval_rate(benchmark_result):
        Processes the evaluation rate from the benchmark result.

    extract_eval_rate(benchmark_result):
        Extracts the evaluation rate from the benchmark result.

    average_eval_rates(eval_rates):
        Calculates and prints the average of the evaluation rates.
    """

    def process_eval_rate(self, benchmark_result):
        """
        Processes the evaluation rate from the benchmark result.

        Parameters
        ----------
        benchmark_result : str
            The benchmark result from which to extract the evaluation rate.

        Returns
        -------
        list
            A list of evaluation rates extracted from the benchmark result.
        """
        eval_rate = self.extract_eval_rate(benchmark_result)
        if eval_rate:
            for rate in eval_rate:
                print(f"◽ Tokens/s:\t{rate}\t📈")
        return eval_rate

    def extract_eval_rate(self, benchmark_result):
        """
        Extracts the evaluation rate from the benchmark result.

        Parameters
        ----------
        benchmark_result : str
            The benchmark result from which to extract the evaluation rate.

        Returns
        -------
        list
            A list of evaluation rates extracted from the benchmark result.
        """
        eval_rate = []
        rate = None
        std_err = benchmark_result.stderr

        for line in std_err.split("\n"):
            if "eval rate" in line and "prompt" not in line:
                match = re.search(r"eval rate:\s+(\d+\.\d+)", line)
                if match:
                    rate = float(match.group(1))
                if rate is not None:
                    eval_rate.append(rate)

        return eval_rate

    def average_eval_rates(self, eval_rates):
        """
        Calculates and prints the average of the evaluation rates.

        Parameters
        ----------
        eval_rates : list
            A list of evaluation rates.

        Returns
        -------
        float
            The average of the evaluation rates. Returns None if the list is empty.
        """
        average = (
            round(sum(eval_rates) / len(eval_rates), 3)
            if eval_rates
            else None
        )
        if average is not None:
            print(f"{'-' * 40}\nAverage eval rate: {average} 📊\n{'-' * 40}\n")

        return average
