# Probability Laboratory (`plab`)

Probability Laboratory is a Python package for exploring probability theory, statistics, and machine learning through mathematical implementations, tests, and educational documentation.

## Current status

Version 0.1.0 is an early-stage project. The probability module currently implements `combinations(n, k)`, which counts unordered selections of `k` distinct objects from `n` distinct objects without replacement. The statistics and machine-learning modules do not yet provide mathematical algorithms; additional probability methods are planned.

## Requirements and installation

Python 3.12 or newer is required. From the repository root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

On Windows (PowerShell), activate with `.venv\Scripts\Activate.ps1` instead.

Install the package in editable mode:

```bash
python -m pip install -e .
```

For development and testing, install the development extras:

```bash
python -m pip install -e ".[dev]"
```

To build the documentation locally, install the documentation extras as well:

```bash
python -m pip install -e ".[dev,docs]"
```

## Basic usage

`combinations(n, k)` calculates the binomial coefficient using exact integer arithmetic:

```python
from plab.probability import combinations

print(combinations(5, 3))  # 10
print(combinations(5, 0))  # 1
print(combinations(3, 5))  # 0
```

For `0 <= k <= n`, the result is `n! / (k! * (n - k)!)`. The function returns `0` when `k > n`.

Inputs must be built-in Python integers (not booleans). Negative values raise `ValueError`; other input types raise `TypeError`. The implementation counts combinations; it does not enumerate the selected subsets.

## Tests and quality checks

From the repository root, with the development extras installed:

```bash
python -m pytest
python -m pytest tests/test_combinatorics.py -v
python -m ruff check .
python -m ruff format --check .
```

To build the MkDocs site after installing the documentation extras:

```bash
python -m mkdocs build --strict
```

## Current limitations

- The current mathematical API consists of `combinations(n, k)`; probability distributions, simulation, statistics, and machine-learning algorithms are not yet implemented.
- `combinations()` accepts only nonnegative built-in integers and returns a count, not a list of combinations.
- This is an early-stage package (version 0.1.0); the API may evolve as more methods are added.

For mathematical background, see [Combinations without replacement](docs/theory/probability.md).