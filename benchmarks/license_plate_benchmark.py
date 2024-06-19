# Standard library imports.
import re

# Local library imports.
from .benchmark import Benchmark


class LicensePlateBenchmark(Benchmark):
    """
    A benchmark class for license plate numbers.
    """

    def __init__(self):
        """
        Initialize the benchmark with a processing function and two dictionaries:
        - 'license_plate_numbers': This dictionary is used to store the processed
                                   results from the benchmark.
        Each processed result (a license plate number) is added as a key in this
        dictionary.

        - 'model_license_plate_numbers': This dictionary is used to store the
                                         license plate numbers associated with
                                         each model.
        The 'store_license_plate' method populates this dictionary by adding the
        model as the key and the 'license_plate_numbers' dictionary as its value.
        """
        super().__init__(self.process_license_plate_number)
        self.license_plate_numbers = []
        self.model_license_plate_numbers = {}

    def extract_license_plate_number(self, stdout):
        """
        Extracts the license plate number from the standard output.

        Args:
            stdout (str): The standard output which may contain the license
            plate number.

        Returns:
            str: The extracted license plate number if found, otherwise None.
        """
        pattern = r"[A-Z0-9]+(?:\s[A-Z0-9]+)*"
        matches = re.findall(pattern, stdout)
        return matches[-1].strip() if matches else None

    def process_license_plate_number(self, benchmark_result):
        """
        Extracts the license plate number from the standard output of a subprocess
        run command and prints it. If no license plate number is found, a message
        is printed and None is returned.

        Args:
            benchmark_result (subprocess.CompletedProcess): The result object returned
            by subprocess.run.

        Returns:
            str: The extracted license plate number, or None if no number was found.
        """
        license_plate_number = self.extract_license_plate_number(
            benchmark_result.stdout
        )
        print(
            f"◽ Plate:\t"
            f"{license_plate_number if license_plate_number else 'not found'} 🚗\n"
        )
        return license_plate_number

    def store_license_plate(self, model, benchmark_result):
        """
        Stores the license plate number for a given model. If a license plate number
        is found in the benchmark result, it is added to the 'license_plate_numbers'
        list and the 'model_license_plate_numbers' dictionary.

        Args:
            model: The model to store the license plate numbers for.
            benchmark_result (subprocess.CompletedProcess): The result object
            returned by subprocess.run.
        """
        license_plate_number = super().process(benchmark_result)
        if license_plate_number is not None:
            self.license_plate_numbers.append(license_plate_number)
        self.model_license_plate_numbers[model] = self.license_plate_numbers
