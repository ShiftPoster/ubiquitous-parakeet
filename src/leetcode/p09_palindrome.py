import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Didnt realize that i could just reverse the ENTIRE number."""
        solution = False
        if x > 0:
            exp = int(math.log10(x))
            upper = x // (10 ** ((exp // 2) + exp % 2))
            lower = 0
            for i in range((exp // 2) + 1):
                big = x // (10 ** i)
                small = big - ((big // 10) * 10)
                lower += small * (10 ** ((exp // 2) - i))
            solution = upper == lower
        elif x == 0:
            solution = True
        return solution


def run(x: int) -> bool:
    return Solution().isPalindrome(x)
