# Standard library imports.
import shutil
import subprocess
import textwrap

# Third party imports.
import yaml


class Ollama:
    @staticmethod
    def is_binary_installed():
        """
        Checks if the ollama binary is present on the system.

        Returns:
            bool: True if ollama binary is present, False otherwise.
        """
        return shutil.which("ollama") is not None

    @staticmethod
    def is_model_installed(model: str):
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
    def read_yaml(yaml_file_path: str):
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
    def run_benchmark(model: str,
                      prompt: str,
                      media_file_path: str) -> subprocess.CompletedProcess:
        """
        Run a benchmark using the specified model, prompt, and media file path.

        Args:
            model (str): The name of the model to use.
            prompt (str): The prompt for the benchmark.
            media_file_path (str): The path to the media file.

        Returns:
            subprocess.CompletedProcess: The result of the benchmark execution.
        """
        benchmark_result = subprocess.run(
            ["ollama", "run", model, prompt + media_file_path, "--verbose"],
            capture_output=True,
            shell=True,
            text=True,
            check=True,
            encoding="utf-8",
        )

        return benchmark_result

    @staticmethod
    def print_prompt(prompt: str) -> None:
        """
        Print the formatted prompt.

        Args:
            prompt (str): The prompt to print.
        """
        section_title = "PROMPT:"
        lines = prompt.strip().splitlines()
        wrapped_lines = [textwrap.fill(
            line, width=40,
            initial_indent=" ",
            subsequent_indent=" "
        ) for line in lines]

        print(section_title)
        for wrapped_line in wrapped_lines:
            print(wrapped_line)
        print("\n")
