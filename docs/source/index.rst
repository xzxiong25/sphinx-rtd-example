
.. Calculator API Documentation main file

Welcome to Calculator API Documentation
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   usage

Project Overview
----------------

This is an example project demonstrating automatic API documentation generation with Sphinx.

Features:

- Automatic documentation from docstrings
- Google-style docstring support
- Source code linking
- Responsive design

Installation
------------

.. code-block:: bash

   pip install -e .

Usage Example
-------------

.. code-block:: python

   from calculator.operations import add, subtract
   from calculator.advanced import factorial

   print(add(5, 3))        # Output: 8
   print(subtract(10, 4))  # Output: 6
   print(factorial(5))     # Output: 120

.. todo::
   Add more examples for advanced functions
