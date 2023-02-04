#!/usr/bin/env python3.8
from collections import Counter
from itertools import accumulate
import math


N,K=map(int, input().split())
A = list(map(int, input().split()))

A = [a % K for a in A]
# print('A', A)
Q = int(input())
queries = []
for i in range(Q):
  l,r=map(int, input().split())
  queries.append((l,r))


counter = Counter(A)
B = [0] + list(accumulate(A))

dp = []
for i in range(N + 1):
  d = [0] * (K + 1)
  dp.append(d)

for i in range(N):
  for j in range(K + 1):
    dp[i +1][j] = dp[i][j]
  dp[i + 1][A[i]] += 1

# for d in dp:
#   print(d)

# print(B)

for query in queries:
  l,r = query
  s = B[r] - B[l - 1]
  ok = False
  cnts = set()
  for j in range(K + 1):
    cnt = dp[r][j] - dp[l - 1][j]
    if cnt != 0 and cnt % K == 0:
      ok = True
    if cnt != 0:
      cnts.add(cnt)
  if len(cnts) == 1:
    ok = True
  if s % K == 0 and ok:
    print('Yes')
  else:
    print('No')

# x = '16 18 33 32 28 26 11'
# print(list(map(int, x.split())))
# print(sum(list(map(int, x.split()))))