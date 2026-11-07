"""
Combinatorics
"""


def combinations(n: int, k: int) -> int:
    """
    Count combinations (unordered selections without replacments)

    Args:
        n: Number of distinct available objects.
        k: Number of objects selected.

    Returns:
        number of combinations.

    Raises:
        TypeError: If n or k is not a built-in integer,
            or either argument is a boolean.
        ValueError: If n or k is negative.

    Examples:
    >>> combinations(n = 5, k = 3)
    10

    Notes:
        Uses a multiplicative algorithm with
        O(min(k, n-k)) iterations for 0 <= k <= n.
        All arithmetic is exact.
    """
    for name, value in (("n", n), ("k", k)):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be nonnegative")

    if k > n:
        return 0

    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i

    return result
