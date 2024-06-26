# Standard library imports.
import re


class EvalRateProcessor:

    @staticmethod
    def process_eval_rate(benchmark_result):
        """
        Extract and process the evaluation rate from a benchmark result.

        Args:
            benchmark_result: Result of the subprocess.run call.

        Returns:
            list: The extracted evaluation rate in a list.
        """
        eval_rate = []
        std_err = benchmark_result.stderr

        for line in std_err.split("\n"):
            if "eval rate" in line and "prompt" not in line:
                match = re.search(r"eval rate:\s+(\d+\.\d+)", line)
                if match:
                    rate = float(match.group(1))
                    eval_rate.append(rate)

        for rate in eval_rate:
            print(f"◽ Tokens/s:\t{rate}\t📈")

        return eval_rate

    @staticmethod
    def average_eval_rates(eval_rates):
        average = (
            round(sum(eval_rates) / len(eval_rates), 3)
            if eval_rates
            else None
        )
        if average is not None:
            print(f"{'-' * 40}\nAverage eval rate: {average} 📊\n{'-' * 40}\n")

        return average
