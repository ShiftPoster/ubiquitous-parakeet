from leetcode.p04_median import riffle


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return riffle.main(nums1, nums2)


def run(nums1: list[int], nums2: list[int]) -> float:
    return Solution().findMedianSortedArrays(nums1, nums2)
