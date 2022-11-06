#!/usr/bin/env python3.8
from itertools import product
S = input()
nums = [int(s) for s in S]

for i in range(2 ** 3):
  s = nums[0]

  k = i
  ans = str(s)
  for j in range(3):
    if k % 2 == 1:
      s += nums[j + 1]
      ans += '+' + str(nums[j + 1])
    else:
      s -= nums[j + 1]
      ans += '-' + str(nums[j + 1])
    k //= 2
  if s == 7:
    ans += '=7'
    print(ans)
    exit()

# perms = list(product(['+', '-'], repeat=3))
# for perm in perms:
#   s = nums[0]
#   for i in range(len(perm)):
#     if perm[i] == '+':
#       s += nums[i + 1]
#     else:
#       s -= nums[i + 1]
#   if s == 7:
#     ans = ''.join(map(str, [nums[0], perm[0], nums[1], perm[1], nums[2], perm[2], nums[3]]))
#     print(ans + '=7')
#     exit()