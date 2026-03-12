from typing import List


def baseline_first_unique_value(nums: List[int]) -> int:
    """
    Baseline A_1
    """
    for value in nums:
        if nums.count(value) == 1:
            return value
    return -1


def baseline_count_subarrays_equal_k(nums: List[int], k: int) -> int:
    """
    Baseline A_2
    """
    count = 0
    n = len(nums)

    for left in range(n):
        for right in range(left, n):
            if sum(nums[left:right + 1]) == k:
                count += 1

    return count