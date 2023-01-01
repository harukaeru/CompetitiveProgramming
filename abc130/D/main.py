#!/usr/bin/env python3.8
import itertools


N, K = map(int, input().split())
A = list(map(int, input().split()))

B = list(itertools.accumulate(A))
B = [0] + B

# print(B)

l = 0
r = 1
cnt = 0
while l <= N and r <= N:
  t = B[r] - B[l]
  if t >= K:
    cnt += (N - r) + 1
    l += 1
  else:
    r += 1
print(cnt)