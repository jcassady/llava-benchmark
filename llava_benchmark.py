# /usr/bin/env/python3

"""
--------------------------------------
⚠️ Custom benchmark class imports.
--------------------------------------
"""
from benchmarks.eval_rate_benchmark import EvalRateBenchmark
from benchmarks.license_plate_benchmark import LicensePlateBenchmark
from modules.llava_benchmark import LlavaBenchmark
from modules.ollama import Ollama


def llava_benchmark(yaml_file_path, benchmarks):
    """
    Runs the LLAVA benchmark for different models, prompts, and images.
    It calculates the average evaluation rates for each model and prints
    the license plate number if found.

    Args:
        yaml_file_path (str): Path to the YAML configuration file.
        benchmarks (list): List of benchmark objects.
    """
    # Check if ollama binary is present.
    if not Ollama.is_binary_installed():
        print(
            "Error: ollama binary not found on the system."
            "Please download it from https://ollama.com/"
        )
        return

    # Read the YAML model data file.
    data = Ollama.read_yaml(yaml_file_path)

    # Extract model names, image file names, and prompts from model data.
    model_names = data["models"]
    image_file_names = data["images"]
    prompts = data["prompts"]

    model_license_plate_numbers = {}

    # Model Processing 🦙
    for model in model_names:
        # Check if the model is installed.
        if not Ollama.is_model_installed(model):
            print(f"Model {model} not found. Skipping this model")
            continue

        print(f"{'=' * 40}\n🦙  MODEL: {model} 🦙\n{'=' * 40}")

        # Prompt + Image Processing 🔄🖼️
        for prompt in prompts:
            for image in image_file_names:
                benchmark_result, image_file_path = Ollama.run_benchmark(
                    model, prompt, image)
                """
                ---------------------------------------------------------------
                ⚠️ IMAGE-LOOP: Call any custom code here that is designed
                                to process or store the benchmark output
                                on a per-image basis.
                ---------------------------------------------------------------
                """
                # Per-Image Benchmark Result Storage 🗃️
                LlavaBenchmark(benchmarks).store_results(
                    benchmark_result, model, image_file_path)

        """
        -----------------------------------------------------------------
        ⚠️ MODEL-LOOP: Call any custom code here that is designed to
                        analyze and report on a per-model basis.
        -----------------------------------------------------------------
        """
        # Per-Model Benchmark Analysis 🔍
        LlavaBenchmark(benchmarks).average_and_plot_benchmarks()


if __name__ == "__main__":
    """
    --------------------------------------------
    ⚠️ Custom benchmark class instantiations
    --------------------------------------------
    Main function that runs the LLaVA benchmark using a
    specified YAML configuration file returning average
    evaluation rates for each model. Custom benchmark
    classes should be appended to the benchmarks list.
    """
    benchmarks = [EvalRateBenchmark(), LicensePlateBenchmark()]
    llava_benchmark("data/config.yml", benchmarks)
