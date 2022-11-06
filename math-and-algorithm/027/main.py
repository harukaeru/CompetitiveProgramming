#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(*A)

# def merge_sort(ary):
#   if len(ary) == 1:
#     return ary
# 
#   mid = len(ary) // 2
#   left = ary[:mid]
#   right = ary[mid:]
# 
#   left = merge_sort(left)
#   right = merge_sort(right)
# 
#   i_l = 0
#   i_r = 0
#   ans = []
#   while i_l < len(left) or i_r < len(right):
#     if i_l == len(left):
#       ans.append(right[i_r])
#       i_r += 1
#     elif i_r == len(right):
#       ans.append(left[i_l])
#       i_l += 1
#     elif left[i_l] <= right[i_r]:
#       ans.append(left[i_l])
#       i_l += 1
#     else:
#       ans.append(right[i_r])
#       i_r += 1
#   return ans
# print(*merge_sort(A))