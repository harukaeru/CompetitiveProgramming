#!/usr/bin/env python3.8
from collections import Counter
from itertools import accumulate


N,K=map(int, input().split())
A = list(map(int, input().split()))

Q = int(input())
queries = []
for i in range(Q):
  l,r=map(int, input().split())
  queries.append((l,r))


dp = []
for i in range(N + 1):
  d = [0] * (K)
  dp.append(d)

for i in range(N):
  for j in range(K):
    dp[i +1][j] = dp[i][j]
  dp[i + 1][i % K] += A[i]

for query in queries:
  l,r = query
  l -= 1
  a = [dp[r][j] - dp[l][j] for j in range(K)]
  b = set(a)
  if len(b) == 1:
    print('Yes')
  else:
    print('No')
# for d in dp:
#   print(d)