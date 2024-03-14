def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left_arr = [el for el in arr if el < pivot ]
    right_arr = [el for el in arr if el > pivot]
    return quick_sort(left_arr) + pivot + quick_sort(right_arr)