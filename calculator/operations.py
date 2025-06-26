
"""Module for basic mathematical operations."""

def add(a, b):
    """Add two numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b

def subtract(a, b):
    """Subtract two numbers.

    Args:
        a (int or float): Minuend
        b (int or float): Subtrahend

    Returns:
        int or float: Difference between a and b

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(10, 2.5)
        7.5
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers.

    Args:
        a (int or float): First factor
        b (int or float): Second factor

    Returns:
        int or float: Product of a and b

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b

def divide(a, b):
    """Divide two numbers.

    Args:
        a (int or float): Dividend
        b (int or float): Divisor

    Returns:
        float: Quotient of a divided by b

    Raises:
        ZeroDivisionError: If divisor is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(5, 2)
        2.5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
