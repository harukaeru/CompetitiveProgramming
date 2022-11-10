#!/usr/bin/env python3.8
import bisect
from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(list)
B = [0] * (N + 1)
for i in range(1, N + 1):
  B[i] = B[i - 1] + A[i - 1]
  counter[B[i]].append(i)

for v in counter.values():
  v.sort()

# print(A)
# print(B)
# print(counter)

cnt = 0
for i in range(N + 1):
  l = B[i]
  r = K + l

  poses = counter[r]
  if not poses:
    continue
  p = bisect.bisect_right(poses, i)
  cnt += len(poses) - p

print(cnt)