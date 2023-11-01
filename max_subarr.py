"""
Maximum Subarray Problem
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example Inputs and Outputs
Example 1
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6

Example 2
Input: nums = [1]
Output: 1

Example 3
Input: nums = [5, 4, -1, 7, 8]
Output: 23

"""

def max_subarray(arr):
    max_sum = arr[0]
    cur_sum = arr[0]
    for i in range(1,len(arr)):
        cur_sum = max(cur_sum + arr[i], arr[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
