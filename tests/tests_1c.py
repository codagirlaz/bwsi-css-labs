"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_sum():
    assert max_subarray_sum([1, 2, 2, 5, 4, 1]) == 15
    assert max_subarray_sum([-5, -7, -10, -6, -1, -3, -2]) == -1
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6