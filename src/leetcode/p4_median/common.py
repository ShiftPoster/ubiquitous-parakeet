def median(nums: list[int], length: int | None = None):
    if length is None:
        length = len(nums)
    if length % 2 == 0:
        median = (nums[(length // 2) - 1] + nums[(length // 2)]) / 2
    else:
        median = nums[(length // 2)]
    return median
