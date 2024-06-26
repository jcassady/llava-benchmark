# Third party imports.
import asciichartpy


class EvalRatePlotter:
    """
    This class is responsible for plotting evaluation rates.

    Attributes:
        None
    """

    def plot(self, eval_rates):
        """
        Plots the evaluation rates as an ASCII line chart.

        Args:
            eval_rates (list): A list of evaluation rates.

        Returns:
            None
        """
        # Upsample the eval_rates list by duplicating each element.
        # This is done to improve the readability of the chart by
        # increasing the number of plot points.
        upsampled_eval_rates = [rate for rate in eval_rates for _ in range(2)]

        print("\t\tY-axis: Evaluation Rates")
        print("\t\tX-axis: Media")
        print(asciichartpy.plot(upsampled_eval_rates, {"width": 40,
                                                       "height": 4,
                                                       "offset": 2,
                                                       "colors": ["\033[31m"]}))
        print("\n")
