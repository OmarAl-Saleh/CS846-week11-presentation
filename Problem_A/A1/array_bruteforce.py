# first_unique_order

from typing import List


def first_unique_value(nums: List[int]) -> int:
    """
    Return the first unique value in the list.
    If none exists, return -1.
    """
    for value in nums:
        if nums.count(value) == 1:
            return value
    return -1


def count_subarrays_equal_k(nums: List[int], k: int) -> int:
    """
    Return the number of contiguous subarrays whose sum equals k.
    A subarray must consist of consecutive elements.
    """
    count = 0
    n = len(nums)

    for left in range(n):
        for right in range(left, n):
            if sum(nums[left:right + 1]) == k:
                count += 1

    return count