#!/usr/bin/env python3.8
from bisect import bisect_left


N,K=map(int, input().split())
A = list(map(int, input().split()))

B = A[:N//2]
C = A[N//2:]

bs = []
for i in range(2 ** len(B)):
  j = i
  k = 0
  for p in range(len(B)):
    if j & (1 << p) != 0:
      k += B[p]
  bs.append(k)

cs = []
for i in range(2 ** len(C)):
  j = i
  k = 0
  for p in range(len(C)):
    if j & (1 << p) != 0:
      k += C[p]
  cs.append(k)

cs.sort()

ok = False
for b in bs:
  req = K - b
  idx = bisect_left(cs, req)
  if len(cs) == idx:
    continue
  if cs[idx] != req:
    continue

  ok = True
  break
if ok:
  print('Yes')
else:
  print('No')