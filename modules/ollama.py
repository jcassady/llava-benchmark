# Standard library imports.
import os
import shutil
import subprocess

# Third party imports.
import yaml


class Ollama:
    def __init__(self):
        pass

    @staticmethod
    def is_binary_installed():
        """
        Checks if the ollama binary is present on the system.

        Returns:
            bool: True if ollama binary is present, False otherwise.
        """
        return shutil.which("ollama") is not None

    @staticmethod
    def is_model_installed(model):
        """
        Checks if a given model is installed.

        Args:
            model (str): The name of the model to check.

        Returns:
            bool: True if the model is installed, False otherwise.
        """
        model_check_result = subprocess.run(
            ["ollama", "show", model],
            capture_output=True,
            shell=True,
            text=True,
            encoding="utf-8",
        )
        return "Error: model" not in model_check_result.stderr

    @staticmethod
    def read_yaml(yaml_file_path):
        """
        Reads a YAML file and returns its content as a dictionary.

        Args:
            yaml_file_path (str): Path to the YAML file.

        Returns:
            dict: Parsed YAML data.
        """
        try:
            with open(yaml_file_path, "r") as yaml_file:
                data = yaml.safe_load(yaml_file)
            return data
        except yaml.YAMLError as e:
            print(e)
            return None

    @staticmethod
    def run_benchmark(model, prompt, image):
        """
        Runs the ollama benchmark with a given image, prompt, and model.

        Args:
            model (str): The name of the model to use.
            prompt (str): The prompt for the benchmark.
            image (str): The name of the image file.

        Returns:
            CompletedProcess: The result of the subprocess.run call.
        """
        image_file_path = os.path.abspath("data\\" + "images\\" + image)
        print(os.path.relpath(image_file_path).upper(), "\t🖼️")
        prompt_with_image = f"{prompt} {image_file_path}"

        # Run the ollama benchmark.
        benchmark_result = subprocess.run(
            ["ollama", "run", model, prompt_with_image, "--verbose"],
            capture_output=True,
            shell=True,
            text=True,
            check=True,
            encoding="utf-8",
        )
        return benchmark_result, image_file_path
