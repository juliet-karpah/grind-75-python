def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    m = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in m:
            return [i, m[nums[i]]]
        m[diff] = i
    return []