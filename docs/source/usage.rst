
.. _usage-guide:

Usage Guide
===========

Basic Usage
-----------

Import basic operations:

.. code-block:: python

   from calculator.operations import add, subtract, multiply, divide

   result = add(10, 5)
   print(result)  # Output: 15

Advanced Functions
------------------

Import advanced math functions:

.. code-block:: python

   from calculator.advanced import power, factorial

   print(power(2, 8))    # Output: 256
   print(factorial(6))    # Output: 720

Error Handling
--------------

Handling division errors:

.. code-block:: python

   try:
       result = divide(10, 0)
   except ZeroDivisionError as e:
       print(f"Error: {e}")  # Output: Error: Cannot divide by zero

Notes
-----

1. All functions support integers and floats
2. Factorial function accepts only non-negative integers
3. Division always returns float
