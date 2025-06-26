
"""Module for advanced mathematical operations."""

def power(base, exponent):
    """Raise base to the power of exponent.

    Args:
        base (int or float): The base number
        exponent (int or float): The exponent

    Returns:
        int or float: Result of the exponentiation

    Examples:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent

def factorial(n):
    """Calculate factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is defined only for non-negative integers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
