from .common import median


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


def main(nums1: list[int], nums2: list[int]) -> float:
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
            upper = data1 if data1.median > data2.median else data2
            lower = data1 if data1.median < data2.median else data2

            mid_nums = lower.nums + upper.nums[: upper.upper]
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

        print(f"{solution  = }")
        reference = []
        reference.extend(nums1)
        reference.extend(nums2)
        reference.sort()
        print("reference =", median(reference), reference)
    return solution
