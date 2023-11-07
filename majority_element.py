def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    m = {}
    for el in nums:
        if el in m:
            m[el] += 1
        else:
            m[el] = 1
    return max(m, key=m.get)