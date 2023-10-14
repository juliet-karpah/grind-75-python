def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    answer = [1] * n
    left = [1] * n
    right = [1] * n
    for i in range(1,n):
        left[i] = nums[i-1] * left[i-1]
    for j in range(n-2, -1, -1):
        right[j] = right[j+1] * nums[j+1]
    return [left[i] * right[i] for i in range(n)]