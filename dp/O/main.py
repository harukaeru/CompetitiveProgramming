#!/usr/bin/env pypy3
mod = 10 ** 9 + 7
N = int(input())
A = []
for i in range(N):
  X = list(map(int, input().split()))
  A.append(X)

dp = [0] * (2 ** N)

dp[0] = 1

for j in range(2 ** N):
  i = bin(j).count('1')
  if i == N:
    continue
  for k in range(N):
    if A[i][k] == 1 and (j >> k) & 1 == 0:
      nex = j | 1 << k
      dp[nex] += dp[j]
      dp[nex] %= mod

# for d in dp:
#   print(d)

print(dp[(1 << N) - 1])