from enum import Enum

import pytest

from leetcode.p09_palindrome import run


class Case(Enum):
    example1 = 121, True
    example2 = -121, False
    example3 = 10, False
    eleven = 11, True
    odd = 123454321, True
    even = 12344321, True

    def __init__(self, x: int, solution: bool) -> None:
        self.x = x
        self.solution = solution


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    assert run(case.x) is case.solution
