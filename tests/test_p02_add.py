"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/
"""

from enum import Enum
from itertools import zip_longest

import pytest

from leetcode.common import ListNode
from leetcode.p02_add import run


class Case(Enum):
    example1 = [2, 4, 3], [5, 6, 4], [7, 0, 8]
    example2 = [0], [0], [0]
    example3 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]

    def __init__(self, l1, l2, sol) -> None:
        self.l1 = l1
        self.l2 = l2
        self.sol = sol


def validate(l1, l2):
    solution = []
    carry = False
    for i, j in zip_longest(l1, l2, fillvalue=0):
        s = i + j
        if carry:
            s += 1
            carry = False
        if s >= 10:
            s -= 10
            carry = True
        solution.append(s)
    if carry:
        solution.append(1)
    return solution


@pytest.mark.parametrize("case", Case)
def test_validate(case: Case):
    assert validate(case.l1, case.l2) == case.sol


def to_linked(ll) -> ListNode:
    ll = list(map(ListNode, ll))
    for i in range(len(ll) - 1):
        ll[i].next = ll[i + 1]
    return ll[0]


def from_linked(ll: ListNode) -> list[int]:
    pylist = []
    curr = ll
    while True:
        val = curr.val
        pylist.append(val)
        if curr.next is None:
            break
        curr = curr.next
    return pylist


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    lll = list(map(to_linked, (case.l1, case.l2)))
    ans = run(lll[0], lll[1])
    assert ans
    assert from_linked(ans) == case.sol


class NoneCase(Enum):
    first = [2, 4, 3], None, [2, 4, 3]
    second = None, [5, 6, 4], [5, 6, 4]
    both = None, None, None

    def __init__(self, l1, l2, sol) -> None:
        self.l1 = l1
        self.l2 = l2
        self.sol = sol


@pytest.mark.parametrize("case", NoneCase)
def test_none(case: Case):
    ans = run(
        None if case.l1 is None else to_linked(case.l1),
        None if case.l2 is None else to_linked(case.l2),
    )
    ans = from_linked(ans) if ans else ans
    assert ans == case.sol
