# llava-benchmark 🌋
[![Pytests](https://github.com/jcassady/llava-benchmark/actions/workflows/pytests.yml/badge.svg)](https://github.com/jcassady/llava-benchmark/actions/workflows/pytests.yml)
[![codecov](https://codecov.io/gh/jcassady/llava-benchmark/graph/badge.svg?token=85L0PEO5MJ)](https://codecov.io/gh/jcassady/llava-benchmark)
[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)



![llava-benchmark](assets/llava-benchmark_logo.png)

## Contents
- [AI Benchmarking Tool 🦙](#ai-benchmarking-tool)
    * [Included Benchmarks](#included-benchmarks)
- [Requirements 📋](#requirements)
- [Cloning the Repository 🚀](#cloning-the-repository)
- [Setting Up the Project](#setting-up-the-project)
- [Configuration 📝](#configuration)
- [Usage 🛠️](#usage)
    * [Command Line 🖥️](#command-line)
- [Documentation 📄](#documentation)
    - [Classes 📚](#classes)
        * [Benchmark class](#benchmark-class)
        * [EvalRateBenchmark class](#evalratebenchmark-class)
        * [LicensePlateBenchmark class](#licenseplatebenchmark-class)
- [Extensibility 🔗](#extensibility)
- [Testing 🧪](#testing)
    * [Running the Tests 🏃](#running-the-tests)
- [Contributing 🤝](#contributing)
- [About 🧑‍💻](#about)
- [License 📄](#license)

## AI Benchmarking Tool

`llava-benchmark` is a general purpose benchmarking tool designed to evaluate AI
image recognition capabilities of [LLaVA](https://github.com/haotian-liu/LLaVA)
models with [Ollama](https://ollama.com).

### Included Benchmarks
* `EvalRateBenchmark`: Measure model image processing speed 📈 
* `LicensePlateBenchmark`: Extract license plate numbers from processed images 🚗

By running these benchmarks, you can quickly assess how well different models
perform in recognizing license plates from images, and how quickly they can do so.

## Requirements

- [Python 3](https://python.org/downloads) 🐍
- [Ollama](https://ollama.com/download) 🦙
- Packages: `asciichartpy`, `os`, `pytest`, `shutil`, `subprocess`, `yaml`

## Cloning the Repository

Before running `llava-benchmark`, clone the repository to your local machine:

1. **Open a Terminal**: On Windows, you can use Command Prompt or PowerShell.
On macOS or Linux, you can use Terminal.

2. **Navigate to the Desired Directory**: Use the `cd` command to navigate to
the directory where you want to clone the repository.

3. **Clone the Repository**: Run the following command to clone the repository:

```bash
git clone https://github.com/jcassady/llava-benchmark.git
```

## Setting Up the Project

Follow these steps after cloning into the local `llava-benchmark/` repo directory:

1. **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        .venv\Scripts\Activate.ps1
        ```
    - On Linux or MacOS:
        ```bash
        source .venv/bin/activate
        ```

3. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```


## Configuration

The tool uses YAML configuration file `data/config.yml` to specify the `models`, `prompts`,
and `images` for the benchmark to use. Here's a brief explanation of each section:

- `models`: This lists the models to be benchmarked
- `prompts`: This lists the prompts to be used for each model
- `images`: This lists the image files to be used in the benchmark

```yaml
# data/config.yml
models:
  - llava:latest
  - llava-llama3:8b
prompts:
  - Read and return the license plate number and letters as text on a new line
images:
  - 1.jpg
  - 2.jpg
```

## Usage
When you execute `llava_benchmark.py`, it performs a series of operations:
1. **Checks if Ollama is Installed**: The script checks if the `ollama` binary is present
on your system. If not, it will print an error message and exit.

2. **Checks if the model is Installed**: For each model specified in the YAML configuration
file, the script checks if the model is installed. If a model is not found, it will print a
message and skip that model.

3. **Runs the Benchmark**: For each model, prompt, and image specified in the YAML
configuration file, the script runs the `ollama` benchmark and stores the evaluation
rate and license plate number (if found).

4. **Prints the Average Evaluation Rate**: After running the benchmark for all models,
prompts, and images, the script prints the average evaluation rate for each model.

5. **Plots the Evaluation Rate Chart**: The script plots an ASCII line chart of the
evaluation rates for visual analysis.

### Command Line
To run the script, navigate to the directory containing the script and type the
following command:

```bash
$ python llava_benchmark.py
========================================
🦙  MODEL: llava:latest 🦙
========================================
DATA\IMAGES\1.JPG 🖼️
◽ Tokens/s: 57.84 📈
◽ Plate: PAX 44 🚗

DATA\IMAGES\2.JPG 🖼️
◽ Tokens/s: 52.79 📈
◽ Plate: OPEC LOL 🚗

DATA\IMAGES\3.JPG 🖼️
◽ Tokens/s: 59.87 📈
◽ Plate: F1 🚗

----------------------------------------
Average eval rate: 56.833 📊
----------------------------------------

                Y-axis: Evaluation Rates
                X-axis: Images
   76.07 ┤
   71.52 ┤             ╭─╮ ╭─
   66.96 ┤             │ │ │
   62.41 ┤ ╭─╮         │ │ │
   57.85 ┼─╯ ╰─╮ ╭─╮ ╭─╯ ╰─╯
   53.30 ┤     ╰─╯ ╰─╯

```


## Documentation
The source code for the project includes comprehensive documentation comments
and docstrings. HTML documentation can be viewed on GitHub Pages:

https://jcassady.github.io/llava-benchmark/ 📄

Please see `__init__.py` file comments for additional
information on how this project loads local module code.  


### Classes
#### Benchmark class
A general-purpose class for processing benchmark results. It's used as a base
class for `EvalRateBenchmark` and `LicensePlateBenchmark` through inheritance.

#### EvalRateBenchmark class
The `EvalRateBenchmark` class is initialized with a method to process the evaluation
rate from a benchmark result. It also initializes an empty list `eval_rates` to store
evaluation rates.

#### LicensePlateBenchmark class

The `LicensePlateBenchmark` class is initialized with a method to process the license
plate number from a benchmark result. It also initializes the list `license_plate_numbers`
to store plate data associated with each model.

#### Extensibility
The project is designed to be easily extendable for other LLaVA image recognition tasks.
This is done through the use of benchmark objects, which are instances of classes that
define specific tasks.

In the main function of `llava_benchmark.py`, instances of `EvalRateBenchmark`
and `LicensePlateBenchmark` are executed after loading the YAML configuration file:
```python
benchmarks = [EvalRateBenchmark(), LicensePlateBenchmark()]
llava_benchmark("data/config.yml", benchmarks)
```
To extend the script for other LLAVA tasks, you can define new benchmark classes that
implement the code needed for those tasks. Then, you can create instances of those
classes and add them to the `benchmarks` list.

## Testing
The `llava-benchmark` module includes a suite of tests to ensure its functionality.
These tests are written using the `pytest` framework and make use of fixtures and
parameterization to test various aspects of the benchmarking process.

### Running the Tests
To run the tests, navigate to the `llava-benchmark/tests/` directory and execute
the following command:
```bash
$ pytest
==================== test session starts =====================
collected 3 items                                                                                                  

test_benchmark.py .                  [ 33%] 
test_eval_rate_benchmark.py .        [ 66%] 
test_license_plate_benchmark.py .    [100%] 

===================== 3 passed in 0.06s ===================== 
```

## Contributing

Contributions are welcome to the `llava-benchmark` project! If you're interested in
contributing, here's how you can do it:

1. **Open an Issue**: If you have a suggestion for an improvement, or you've found
a bug, start by opening an issue in the project repository. Describe your suggestion
or bug report in detail.

2. **Discussion**: Once the issue is opened, maintainers of the project or other
contributors will review the issue and discuss it.

3. **Implementation**: If your suggestion is accepted, you or someone else can
start working on implementing it.

We appreciate your help in making the LLAVA Benchmark project better!

## About 

[Jordan Cassady](https://jordan.cassady.me) is a Canadian Network Engineer
with a decade of startup experience automating test systems aligned to
company KPIs.  If you’ve got a puzzle to solve, a codebase to conquer,
or a moonshot idea, count me in. Let’s connect! ✌️

👉 https://www.linkedin.com/in/jordancassady/


## License

This project is licensed under the terms of the MIT license.
