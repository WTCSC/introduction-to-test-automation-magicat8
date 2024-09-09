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
@pytest.mark.parametrize("number1, expected", [(4, True),(3, False),(6, True)])
def test_is_even(number1, expected):
  """
  Tests for the `is_even` function
  """
  assert is_even(number1) == expected

@pytest.mark.parametrize("number2, expected", [(3, True),(2, False),(7, True)])
def test_is_odd(number2, expected):
  """
  Tests for the `is_odd` function
  """
  assert is_odd(number2) == expected

@pytest.mark.parametrize("number_list, expected", [([2,3,5,7,9,8,3], 5.285714285714286)])
def test_mean(number_list, expected):
  """
  Tests for the `mean` function
  """
  assert mean(number_list) == expected

@pytest.mark.parametrize("number_list1, expected", [([2,3,5,7,9,8,3], 5)])
def test_median(number_list1, expected):
  """
  Tests for the `median` function
  """
  assert median(number_list1) == expected

@pytest.mark.parametrize("number_list2, expected", [([2,3,5,7,9,8,3], [3])])
def test_mode(number_list2, expected):
  """
  Tests for the `mode` function
  """
  assert mode(number_list2) == expected