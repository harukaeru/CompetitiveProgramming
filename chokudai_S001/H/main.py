#!/usr/bin/env python3.8

from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

L = [1e18] * N
for i in range(N):
  idx = bisect_left(L, A[i])
  L[idx] = min(L[idx], A[i])

ans = 0
for i in range(N):
  if L[i] == 1e18:
    break
  ans += 1
print(ans)