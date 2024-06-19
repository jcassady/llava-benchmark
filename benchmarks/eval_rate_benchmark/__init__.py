"""
This is the __init__.py file for the `eval_rate_benchmark` package,
which is a part of the larger project.

The `eval_rate_benchmark` package is located in the `benchmarks` directory.
It contains the `EvalRateBenchmark` class, which is used to evaluate the rate
of a model as part of the benchmarking process.

The `EvalRateBenchmark` class is imported here to make it accessible when the
`eval_rate_benchmark` package is imported elsewhere in the project. This allows
for a cleaner import statement, as you can directly import the `EvalRateBenchmark`
class from the `eval_rate_benchmark` package.

For example, instead of using:
    from benchmarks.eval_rate_benchmark.eval_rate_benchmark import EvalRateBenchmark
you can use:
    from benchmarks.eval_rate_benchmark import EvalRateBenchmark
"""

from .eval_rate_benchmark import EvalRateBenchmark
