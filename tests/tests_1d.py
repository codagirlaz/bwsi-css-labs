"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([1, 2, 2, 5, 4, 1], 9) == [3, 4]
    assert two_sum([-5, -7, -10, -6, -1, -3, -2], -13) == [1, 3]