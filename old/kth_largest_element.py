import queue
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    maxheap = queue.PriorityQueue()
    for el in nums:
        maxheap.put(el)
    for i in range(0, len(nums)-k):
        maxheap.get()
    return maxheap.get()
    
print(findKthLargest([3,2,3,1,2,4,5,5,6],4))