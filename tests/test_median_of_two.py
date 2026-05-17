"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""
from enum import Enum
from typing import Iterator

import pytest


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


def median(nums: list[int], length: int | None = None):
    if length is None:
        length = len(nums)
    if length % 2 == 0:
        median = (nums[(length // 2) - 1] + nums[(length // 2)]) / 2
    else:
        median = nums[(length // 2)]
    return median


def slow(l1: list[int], l2: list[int]) -> float:
    """Python's sort method is O(n log n), but it will help validate that the test cases I added are correct."""
    new = []
    new.extend(l1)
    new.extend(l2)
    new.sort()
    return median(new)


@pytest.mark.parametrize("case", Case)
def test_slow(case: Case):
    assert slow(case.l1, case.l2) == case.sol


class Data:
    nums: list[int]
    lower: int
    middle: float
    upper: int
    median: int
    length: int

    @property
    def odd(self) -> bool:
        return int(self.middle) == self.middle

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.length = len(self.nums)
        self.middle = (self.length - 1) / 2
        if self.middle == 0:
            self.upper = self.lower = int(self.middle)
        else:
            self.upper = int(self.middle) + 1
            self.lower = int(self.middle)
            self.lower -= 1 if self.odd else 0
        if self.odd:
            self.median = self.nums[int(self.middle)]
        else:
            self.median = int(sum(self.nums[self.lower : self.upper + 1]) / 2)

    def __repr__(self):
        asdict = vars(self)
        pad = max(map(len, asdict.keys()))
        parts = (
            f"{self.__class__.__name__}()",
            *(f"   {attr:<{pad}} : {value}" for attr, value in asdict.items()),
            ")",
        )
        return "\n".join(parts)


def sort_gen(nums1: list[int], nums2: list[int]) -> Iterator[int]:
    nums1_iter = iter(nums1)
    nums2_iter = iter(nums2)
    curr1 = None
    curr2 = None
    while True:
        if curr1 is None and nums1_iter is not None:
            try:
                curr1 = next(nums1_iter)
            except StopIteration:
                nums1_iter = None

        if curr2 is None and nums2_iter is not None:
            try:
                curr2 = next(nums2_iter)
            except StopIteration:
                nums2_iter = None

        if nums1_iter is None and nums2_iter is None:
            break
        elif curr1 is None and curr2 is None:
            break
        elif curr1 is None:
            yield curr2
            curr2 = None
        elif curr2 is None:
            yield curr1
            curr1 = None
        elif curr1 < curr2:
            yield curr1
            curr1 = None
        else:
            yield curr2
            curr2 = None


class Solution:
    def mid_solution(self, upper: Data, lower: Data):
        mid_nums = lower.nums + upper.nums[:upper.upper]
        mid_nums = filter(lambda x: x <= upper.median, mid_nums)

        mid_nums = list(mid_nums)
        mid_nums.sort()
        print(f"{mid_nums = }")
        middle_i = (len(lower.nums) + len(upper.nums) - 1) / 2
        print(f"{middle_i = }")

        if middle_i == int(middle_i):
            solution = mid_nums[int(middle_i)]
        else:
            solution = (mid_nums[int(middle_i) + 1] + mid_nums[int(middle_i)]) / 2
        return solution

    def backup(self, nums1: list[int], nums2: list[int]) -> float:
        solution = 0
        if len(nums1) == len(nums2) == 1:
            solution = (nums1[0] + nums2[0]) / 2
        else:
            data1 = Data(nums1)
            data2 = Data(nums2)
            print(f"{data1 = }")
            print(f"{data2 = }")
            if data1.median == data2.median:
                solution = data1.median
            else:
                # upper = data1 if data1.median > data2.median else data2
                # lower = data1 if data1.median < data2.median else data2
                # solution = self.mid_solution(upper, lower)

                gen = sort_gen(nums1, nums2)

                middle_i = (len(nums1) + len(nums2) - 1) / 2
                print(f"{middle_i = }")
                for _ in range(int(middle_i)):
                    # skip
                    next(gen)
                solution = next(gen)
                # if even
                if middle_i != int(middle_i):
                    solution = (solution + next(gen)) / 2

            print(f"{solution  = }")
            reference = []
            reference.extend(nums1)
            reference.extend(nums2)
            reference.sort()
            print("reference =", median(reference), reference)
        return solution

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        gen = sort_gen(nums1, nums2)

        middle_i = (len(nums1) + len(nums2) - 1) / 2
        print(f"{middle_i = }")
        for _ in range(int(middle_i)):
            # skip
            next(gen)
        solution = next(gen)
        # if even
        if middle_i != int(middle_i):
            solution = (solution + next(gen)) / 2

        return solution


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    ans = Solution().findMedianSortedArrays(case.l1, case.l2)
    assert ans == case.sol
