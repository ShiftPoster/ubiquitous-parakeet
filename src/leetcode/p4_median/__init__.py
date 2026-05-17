from leetcode.p4_median import sort_gen


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return sort_gen.main(nums1, nums2)


def run(nums1: list[int], nums2: list[int]) -> float:
    return Solution().findMedianSortedArrays(nums1, nums2)
