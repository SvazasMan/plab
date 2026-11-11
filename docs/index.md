# Probability Laboratory

Probability Laboratory (`plab`) is a Python project for exploring probability theory, statistics, and machine learning through mathematical implementations, tests, and educational documentation.

## Objectives

- Implement mathematical algorithms in Python.
- Explain the underlying mathematical theory.
- Test correctness and numerical behavior.
- Compare implementations with established libraries.
- Provide reproducible educational examples.

## Project areas

### Probability Theory

Combinatorics is the first implemented area. Probability spaces, distributions, expectation, and simulation remain future work.

### Statistics

Descriptive statistics, estimation, and hypothesis testing are planned; no statistics algorithms are implemented yet.

### Machine Learning

Optimization, regression, and learning algorithms are planned; no machine-learning algorithms are implemented yet.

## Current status

Version 0.1.0 includes `plab.probability.combinations(n, k)` for counting unordered selections of distinct objects without replacement. The function uses exact integer arithmetic.

## Installation

Python 3.12 or newer is required. From the cloned repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
python -m pip install -e .
```

On Windows PowerShell, activate the environment using `.venv\Scripts\Activate.ps1` instead. For development and documentation dependencies, install `python -m pip install -e ".[dev,docs]"`.

## Basic usage

```python
from plab.probability import combinations

combinations(5, 3)  # 10
combinations(5, 0)  # 1
combinations(3, 5)  # 0
```

For `0 <= k <= n`, this computes the binomial coefficient `n! / (k! * (n - k)!)`. When `k > n`, the result is `0`. See [Probability theory](theory/probability.md) for the derivation and computational approach and [API reference](api/index.md) for the function documentation.

## Tests and quality checks

After installing the development dependencies, run these commands from the repository root:

```bash
python -m pytest
python -m pytest tests/test_combinatorics.py -v
python -m ruff check .
python -m ruff format --check .
```

With the documentation dependencies installed, validate the documentation build:

```bash
python -m mkdocs build --strict
```

## Current limitations

- `combinations()` is the only implemented mathematical method so far; statistics, machine-learning, and other probability algorithms are planned.
- The function accepts nonnegative built-in integers only. Boolean or non-integer inputs raise `TypeError`, and negative inputs raise `ValueError`.
- The function returns an exact count, not the combinations themselves.
- The package is at version 0.1.0, and its interface may change as development continues.