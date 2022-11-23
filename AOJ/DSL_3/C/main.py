#!/usr/bin/env python3.8
N, Q = map(int, input().split())
A = list(map(int, input().split()))
Q = list(map(int, input().split()))

B = [0] * (1 + N)
for i in range(1, N + 1):
  B[i] = A[i - 1] + B[i - 1]

for q in Q:
  cnt = 0
  l = 0
  r = 1
  while l < len(B):
    if r < len(B) and B[r] - B[l] <= q:
      cnt += (r - l)
      r += 1
    else:
      l += 1
  print(cnt)
