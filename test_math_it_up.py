import pytest
from math_it_up import is_even, is_odd, mean, median, mode

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""
def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert is_even(4) == True

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert is_odd(3) == True 


def test_mean():
  """
  Tests for the `mean` function
  """
  assert mean([2,3,5,7,9,8,3]) == 5.285714285714286

def test_median():
  """
  Tests for the `median` function
  """
  assert median([2,3,5,7,9,8,3]) == 5

def test_mode():
  """
  Tests for the `mode` function
  """
  assert mode([2,3,5,7,9,8,3]) == [3]