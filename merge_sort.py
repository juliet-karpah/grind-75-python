def merge(a1,a2):
  res = []
  i = j = 0
  while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
      res.append(a1[i])
      i += 1
    else:
      res.append(a2[j])
      j += 1
  while i < len(a1):
    res.append(a1[i])
    i += 1

  while j < len(a2):
    res.append(a2[j])
    j += 1

  return res

def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  left_res = merge_sort(left_arr)
  right_res = merge_sort(right_arr)
  return merge(left_res, right_res)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
arr = merge_sort(arr)
print("Sorted array:", arr)