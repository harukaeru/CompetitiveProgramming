#!/usr/bin/env pypy3
import bisect

N = int(input())
L = list(map(int, input().split()))

L.sort()

tot = 0
for i in range(N - 1):
  for j in range(i + 1, N):
    a = L[i]
    b = L[j]
    ma = a + b 
    mi = abs(a - b)

    big = bisect.bisect_left(L, ma)
    small = max(bisect.bisect_right(L, mi), j + 1)
    if big <= small:
      continue
    tot += big - small
print(tot)
