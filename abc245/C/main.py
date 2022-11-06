#!/usr/bin/env python3.8
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [A[0], B[0]]
for i in range(1, N):
  ndp = set()
  for d in dp:
    if abs(A[i] - d) <= K:
      ndp.add(A[i])
    if abs(B[i] - d) <= K:
      ndp.add(B[i])
  dp = list(ndp)

if len(dp) >= 1:
  print('Yes')
else:
  print('No')