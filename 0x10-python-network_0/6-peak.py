#!/usr/bin/python3
""" script for finding the peak of a list """

def find_peak(nums):
    """
        a function to find a peak of a list by iterating over all the elements untill
        we meet the condition
    """
    length = len(nums)
    if not isinstance(nums, list) or length == 0:
        return None
    if length == 2:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[2]
    elif length == 1:
        return nums[0]

    peak = nums[0]

    for n in range(1, length - 1):
        if nums[n] > nums[n - 1] and nums[n] > nums[n + 1]:
            return nums[n]
    return peak
