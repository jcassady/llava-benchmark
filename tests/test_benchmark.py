import pytest
import random
from unittest.mock import Mock
from benchmarks.benchmark import Benchmark

# Define a method to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

@pytest.fixture
def benchmark():
    # This is a fixture for the Benchmark object, which is
    # used to process the evaluation rates from the LLaVA model.
    # Initialize the Benchmark object with the calculate_average method.
    return Benchmark(calculate_average)

@pytest.fixture
def benchmark_result():
    # The numbers in the list are mock evaluation rates from processing
    # images with the LLaVA model. Generate a list of 10 random evaluation
    # rates between 0.01 and 100.00.
    return [round(random.uniform(0.01, 100.00), 2) for _ in range(10)]

def test_benchmark_process(benchmark, benchmark_result):
    # The result is the processed evaluation rate from the mock LLaVA model.
    result = benchmark.process(benchmark_result)

    # The expected value is the average of the evaluation rates from
    # the mock LLaVA model.
    expected = calculate_average(benchmark_result)

    # The expected result is the average evaluation rate from the
    # mock LLaVA model.
    assert result == expected, f"Expected {expected}, but got {result}"
