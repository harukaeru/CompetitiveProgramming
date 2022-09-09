def _quick_sort(arr, left, right):
  if right - left <= 1:
    return

  pivot_idx = right - 1
  separator = left

  # [3, 4, -1,...], [9, 10, ...]
  for i in range(left, right - 1):
    if arr[i] < arr[pivot_idx]:
      arr[i], arr[separator] = arr[separator], arr[i]
      separator += 1
  arr[separator], arr[pivot_idx] = arr[pivot_idx], arr[separator]

  _quick_sort(arr, left, separator)
  _quick_sort(arr, separator + 1, right)

def quick_sort(N):
  _quick_sort(N, 0, len(N))

N = [3, 4, -1, 9, 10, 12, 8, 12, 12, 5, 8, 7, 2, 20, 7]

ans = sorted(N)
quick_sort(N)
print(N)
assert N == ans