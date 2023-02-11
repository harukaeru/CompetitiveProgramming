#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = map(int, input().split())
X = int(input())

B = set(B)

dp = [False] * (1 + X)

dp[0] = True

for i in range(X):
  if not dp[i]:
    continue

  for j in range(N):
    nex = i + A[j]
    if nex <= X and nex not in B:
      dp[i + A[j]] = True

# print(dp)
if dp[X]:
  print('Yes')
else:
  print('No')