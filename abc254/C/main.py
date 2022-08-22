#!/usr/bin/env python3
N, K = map(int, input().split())
B = list(map(int, input().split()))
A = [b for b in B]
B = list(sorted(B))

ks = {}
for i in range(N):
  ks.setdefault(i % K, []).append(A[i])

for v in ks.values():
  v.sort()
  v.reverse()

ans = []
for i in range(N):
  ans.append(ks[i % K].pop())

if ans == B:
  print('Yes')
else:
  print('No')