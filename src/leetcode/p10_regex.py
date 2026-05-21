import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, re.escape(s)) is not None


def run(s: str, p: str) -> bool:
    return Solution().isMatch(s, p)
