import math

import pytest

from plab.probability.combinatorics import combinations


@pytest.mark.parametrize(
    ("n", "k", "expected"),
    [
        (0, 0, 1),
        (5, 0, 1),
        (5, 5, 1),
        (5, 3, 10),
        (10, 2, 45),
        (3, 5, 0),
        (30, 15, 155117520),
    ],
)
def test_known_results(n, k, expected):
    assert combinations(n, k) == expected


@pytest.mark.parametrize(
    ("n", "k"),
    [
        (5, -1),
        (-5, 2),
        (-1, -1),
    ],
)
def test_negative_inputs(n, k):
    with pytest.raises(ValueError):
        combinations(n, k)


@pytest.mark.parametrize(
    ("n", "k"),
    [
        (5.0, 2),
        (5, 2.0),
        ("5", 2),
        (True, 1),
        (5, False),
        (None, 1),
    ],
)
def test_invalid_types(n, k):
    with pytest.raises(TypeError):
        combinations(n, k)


@pytest.mark.parametrize("n", range(0, 30))
def test_boundary_identities(n):
    assert combinations(n, 0) == 1
    assert combinations(n, n) == 1


@pytest.mark.parametrize("n", range(0, 30))
def test_symmetry(n):
    for k in range(n + 1):
        assert combinations(n, k) == combinations(n, n - k)


@pytest.mark.parametrize("n", range(2, 30))
def test_pascals_identity(n):
    for k in range(1, n):
        assert combinations(n, k) == (
            combinations(n - 1, k - 1) + combinations(n - 1, k)
        )


@pytest.mark.parametrize("n", range(0, 50))
def test_against_python_math(n):
    for k in range(n + 3):
        assert combinations(n, k) == math.comb(n, k)
