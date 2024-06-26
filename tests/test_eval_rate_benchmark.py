import pytest
from unittest.mock import Mock
from benchmarks.eval_rate_benchmark import EvalRateBenchmark


# This fixture creates an instance of the EvalRateBenchmark class
# from the 'benchmarks' module.
# The instance will be used in the test function to run the benchmark
# and store the results.
@pytest.fixture
def benchmark():
    return EvalRateBenchmark()


# This fixture creates a mock benchmark result with a predefined 'stderr' attribute.
# The 'stderr' attribute is set to mimic the output of a real benchmark.
# The mock benchmark result will be used in the test function to simulate
# a real benchmark result.
@pytest.fixture
def benchmark_result():
    result = Mock()
    result.stderr = """
    total duration:       538.5513ms
    load duration:        11.508ms
    prompt eval count:    1 token(s)
    prompt eval duration: 459.674ms
    prompt eval rate:     2.18 tokens/s
    eval count:           4 token(s)
    eval duration:        64.913ms
    eval rate:            61.62 tokens/s
    """
    return result


# Parameterize the test function
# This allows the test function to run multiple times with different expected results.
# In this case, it only runs once with the expected result of 61.62 tokens/s.
@pytest.mark.parametrize("expected", [[61.62]])
def test_eval_rate_benchmark_process(benchmark, benchmark_result, expected):
    # The store_eval_rate method of the benchmark object is called with the
    # 1. benchmark_result as an argument.
    # 2. "data/images/1.jpg": The path to the image file.
    # The result is then compared to the expected result to verify the
    # correctness of the store_eval_rate method.
    benchmark.process_eval_rate(benchmark_result)
    benchmark.store_eval_rate("data/images/1.jpg")

    # If the assertion fails, an AssertionError will be raised with a
    # message indicating the expected and actual results.
    assert benchmark.current_eval_rate == expected, f"Expected {expected}, but got {benchmark.current_eval_rate}"
