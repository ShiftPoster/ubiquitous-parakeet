from typing import Iterator

# from .midsection import Data


def riffle_sort(nums1: list[int], nums2: list[int]) -> Iterator[int]:
    """I think this is O(n1 +  n2)."""
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
            # not sure why this gets a type error, curr2 cant be None as well
            yield curr2  # type: ignore
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


def main(nums1: list[int], nums2: list[int]) -> float:

    gen = riffle_sort(nums1, nums2)

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
