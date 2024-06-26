# /usr/bin/env/python3

import argparse
import os

"""
--------------------------------------
⚠️ Custom benchmark class imports.
--------------------------------------
"""
from benchmarks.eval_rate_benchmark import EvalRateBenchmark
from benchmarks.license_plate_benchmark import LicensePlateBenchmark
from benchmarks.call_audio_benchmark import CallAudioBenchmark
from modules.llava_benchmark import LlavaBenchmark
from modules.ollama import Ollama


def llava_benchmark(yaml_file_path, benchmarks):
    """
    Runs the LLAVA benchmark for different models, prompts, and media
    files. It calculates the average evaluation rates in tokens/s for
    each model and prints license plate or call audio benchmark results.

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

    # Extract model names, media file names, and prompts from model data.
    model_names = data["models"]
    media_file_names = data["media"]
    prompts = data["prompts"]

    model_license_plate_numbers = {}

    # Model Processing 🦙
    for model in model_names:
        # Check if the model is installed.
        if not Ollama.is_model_installed(model):
            print(f"Model {model} not found. Skipping this model")
            continue

        print(f"{'=' * 40}\n🦙  MODEL: {model} 🦙\n{'=' * 40}")

        # Prompt + Media Processing 🔁
        for prompt in prompts:
            Ollama.print_prompt(prompt)
            for media in media_file_names:
                transcript, media_file_path = LlavaBenchmark(
                    benchmarks).process_media(media)

                print(os.path.relpath(media_file_path).upper(), "\t📁")

                benchmark_result = Ollama.run_benchmark(
                    model, prompt + transcript, media_file_path)
                """
                ---------------------------------------------------------------
                ⚠️ MEDIA-LOOP: Call any custom code here that is designed
                                to process or store the benchmark output
                                on a per-image basis.
                ---------------------------------------------------------------
                """
                # Per-Media Benchmark Result Storage 🗃️
                LlavaBenchmark(benchmarks).store_results(
                    benchmark_result, model, media_file_path)

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
    Run the LLaVA benchmark using a specified YAML
    configuration file, returning average evaluation
    rates for each model. Custom benchmark classes
    should be added here.

    Usage:
        1. Create a YAML configuration file (e.g.,
           config_license_plates.yml or config_calls.yml)
           in the 'data/' directory.
        2. Specify the media type using the '--media'
           argument:
           - For license plates:
             python llava_benchmark.py --media license_plates
           - For call audio:
             python llava_benchmark.py --media call_audio
    """
    parser = argparse.ArgumentParser(description="LLaVA Benchmark")
    parser.add_argument(
        "--media",
        choices=["license_plates", "call_audio"],
        required=True,
        help="Specify the media type (license_plates or call_audio)")
    args = parser.parse_args()

    if args.media == "license_plates":
        benchmarks = [EvalRateBenchmark(), LicensePlateBenchmark()]
        llava_benchmark("data/config_licence_plates.yml", benchmarks)
    elif args.media == "call_audio":
        benchmarks = [EvalRateBenchmark(), CallAudioBenchmark()]
        llava_benchmark("data/config_call_audio.yml", benchmarks)
