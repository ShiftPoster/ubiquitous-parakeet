from enum import Enum

import pytest

from leetcode.p10_regex import run


class Case(Enum):
    example1 = "aa", "a", False
    example2 = "aa", "a*", True
    example3 = "ab", ".*", True

    def __init__(self, string: str, pattern: str, solution: bool) -> None:
        self.string = string
        self.pattern = pattern
        self.solution = solution


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    assert run(case.string, case.pattern) is case.solution
