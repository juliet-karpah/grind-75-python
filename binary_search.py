def binary_search(data, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)
