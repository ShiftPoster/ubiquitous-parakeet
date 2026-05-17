"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

from enum import Enum

import pytest

from leetcode.p4_median import run
from leetcode.p4_median.common import median


class Case(Enum):
    example1 = [1, 3], [2], 2.0
    example2 = [1, 2], [3, 4], 2.5
    lopsided = [9, 9, 9, 9, 9, 9, 9], [1, 1, 1, 1], 9
    shuffle = [1, 3, 5], [2, 4, 6], 3.5
    lopshuff = [1, 1, 1, 3, 5], [2, 4, 6], 2.5
    donut = [1, 1, 1, 9, 9, 9], [4, 5, 6], 5
    decept = [1, 1, 9], [4, 5, 6], 4.5
    single = [1], [3], 2
    edge1 = [4], [1, 6, 7, 8, 9], 6.5
    edge2 = [1, 1, 8, 9], [1, 1, 4, 5], 2.5

    def __init__(self, l1, l2, sol) -> None:
        self.l1 = l1
        self.l2 = l2
        self.sol = sol


def baseline(l1: list[int], l2: list[int]) -> float:
    """Python's sort method is O(n log n), but it will help check that the test cases I added are correct."""
    new = []
    new.extend(l1)
    new.extend(l2)
    new.sort()
    return median(new)


@pytest.mark.parametrize("case", Case)
def test_baseline(case: Case):
    assert baseline(case.l1, case.l2) == case.sol


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    assert run(case.l1, case.l2) == case.sol
