# Standard library imports.
import os
import re

class LicensePlateBenchmark:
    """
    A benchmark class for license plate numbers.

    Attributes:
        current_license_plate_number (str): The current license plate number being processed.
        license_plate_numbers (list): List of extracted license plate numbers.
        model_license_plate_numbers (dict): Mapping of model names to license plate numbers.
    """

    def __init__(self):
        """
        Initialize LicensePlateBenchmark instance.
        """
        self.current_license_plate_number = None
        self.license_plate_numbers = []
        self.model_license_plate_numbers = {}

    @staticmethod
    def media_file_path(media_file: str) -> str:
        """
        Get the absolute path to a media file.

        Args:
            media_file (str): The name of the media file.

        Returns:
            str: Absolute path to the media file.
        """
        return os.path.abspath(os.path.join("data", "images", media_file))

    def extract_license_plate_number(self, stdout) -> str:
        """
        Extract the license plate number from benchmark result output.

        Args:
            stdout (str): Benchmark result output.

        Returns:
            str: Extracted license plate number or None if not found.
        """
        pattern = r"failed to get console mode for stderr: The handle is invalid\." \
                  r"\n(.*)"
        match = re.search(pattern, stdout)
        return match.group(1).strip() if match else None

    def process_license_plate_number(self, benchmark_result: str) -> None:
        """
        Process the license plate number from benchmark result.

        Args:
            benchmark_result (str): Result of the benchmark execution.
        """
        self.current_license_plate_number = self.extract_license_plate_number(
            benchmark_result.stdout
        )
        print(
            f"◽ Plate:\t{self.current_license_plate_number or 'not found'}\t🚗\n")

    def store_license_plate(self, model: str, benchmark_result: str) -> None:
        """
        Store the license plate number for a specific model.

        Args:
            model (str): Model name.
            benchmark_result (str): Result of the benchmark execution.
        """
        self.process_license_plate_number(benchmark_result)
        if self.current_license_plate_number is not None:
            self.license_plate_numbers.append(
                self.current_license_plate_number)
        self.model_license_plate_numbers[model] = self.license_plate_numbers

