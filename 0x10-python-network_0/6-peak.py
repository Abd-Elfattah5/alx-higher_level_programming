#!/usr/bin/python3
""" script for finding the peak of a list """

def find_peak(nums):
    """
        a function to find a peak of a list by iterating over all the elements
    """
    if not isinstance(nums, list) or len(nums) == 0:
        return None
    peak = nums[0]

    for n in nums:
        if n > peak:
            peak = n
    return peak
