# __init__.py

"""
This __init__.py file marks the 'tests' directory as a Python package, enabling
it to be imported as a module. 

In the context of pytest and this project:
1. If tests need to import the 'EvalRateBenchmark' and 'LicensePlateBenchmark'
   classes from the 'benchmarks' module, this directory needs to be a package
   for these imports to work correctly.
2. If tests are run with 'python -m pytest', this directory needs to be a
   package because the '-m' option runs Python modules.
"""
