from enum import Enum

import pytest

from leetcode.common import ListNode
from leetcode.p23_merge_k import run


class Case(Enum):
    example1 = [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]
    example2 = [], []
    example3 = [[]], []
    example4 = [[], [1]], [1]

    def __init__(self, k: list[list[int]], sol: list[int]) -> None:
        self.k = k
        self.sol = sol


@pytest.mark.parametrize("case", Case)
def test_solution(case: Case):
    ans = run([ListNode.from_list(_) if _ else None for _ in case.k])
    if isinstance(ans, ListNode):
        ans = ans.to_list()
    elif ans is None:
        ans = []
    else:
        raise TypeError(ans)
    assert ans == case.sol
