#!/usr/bin/env python3
from collections import defaultdict
N, X = map(int, input().split())
L = []
A = []
for i in range(N):
  l, *a = map(int, input().split())
  L.append(l)
  A.append(a)

dp = [defaultdict(int) for i in range(N + 1)]
dp[0][1] = 1
for i in range(N):
  for a in A[i]:
    for prev, count in dp[i].items():
      dp[i + 1][prev * a] += count
  
print(dp[N][X])