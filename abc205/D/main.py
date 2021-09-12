#!/usr/bin/env python3
import bisect
N, Q = map(int, input().split())
*A, = map(int, input().split())

A = [0] + A + [2 * 10**18+1]

# print('A', A)
diffs = []
for i in range(1, len(A)):
    max_left = A[i - 1] + 1
    min_right = A[i] - 1
    if max_left > min_right:
        continue
    diff = (max_left, min_right)
    diffs.append(diff)

# print('diffs', diffs)

nums = []
for d in diffs:
    nums.append(d[1] - d[0] + 1)

sss = [0] * (len(nums) + 1)
for i in range(len(nums)):
    sss[i+1] = nums[i] + sss[i]

# print(nums)
# print(sss)

for i in range(Q):
    q = int(input())
    left_idx = bisect.bisect_left(sss, q)
    idx = (q - sss[left_idx - 1]) - 1
    # print('lf', left_idx - 1)
    diff = diffs[left_idx - 1]
    print(diff[0] + idx)
