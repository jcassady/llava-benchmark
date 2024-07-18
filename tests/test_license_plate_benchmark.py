import pytest
from unittest.mock import Mock
from benchmarks.license_plate_benchmark import LicensePlateBenchmark

# This fixture creates an instance of the LicensePlateBenchmark class
# from the 'benchmarks' module. The instance will be used in the test
# function to run the benchmark and store the results.


@pytest.fixture
def benchmark():
    return LicensePlateBenchmark()

# This fixture creates a mock benchmark result with a predefined 'stdout'
# attribute.
# The 'stdout' attribute is set to mimic the output of a real benchmark.
# The mock benchmark result will be used in the test function to simulate
# a real benchmark result.


@pytest.fixture
def benchmark_result():
    result = Mock()
    result.stdout = "failed to get console mode for stderr:" \
                    "The handle is invalid.\n" \
                    "CRAIG"
    return result

# This allows the test function to run multiple times with different
# expected results.
# In this case, it only runs once with the expected result of "CRAIG".


@pytest.mark.parametrize("model,expected", [("llava:latest", "CRAIG")])
def test_license_plate_benchmark_store(benchmark,
                                       benchmark_result,
                                       model,
                                       expected):
    # Use the benchmark and benchmark_result fixtures
    # The store_license_plate method of the benchmark object is called
    # with the model and the benchmark_result as arguments.
    # The result is then compared to the expected result to verify the
    # correctness of the store_license_plate method.
    benchmark.store_license_plate(model, benchmark_result)

    # Assert that the license plate number is stored correctly
    # If the assertion fails, an AssertionError will be raised
    # with a message indicating the expected and actual results.
    assert benchmark.current_license_plate_number == expected
    # assert benchmark.license_plate_numbers == expected
    # assert benchmark.model_license_plate_numbers[model] == expected
