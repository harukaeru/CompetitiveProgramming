#!/usr/bin/env python3
import bisect
N = int(input())
S = [s == '1' for s in list(input())]
W = list(map(int, input().split()))

adults = []
children = []
for i in range(N):
  if S[i]:
    adults.append(W[i])
  else:
    children.append(W[i])

adults.sort()
children.sort()

max_m = 0
for w in W:
  for d in (1, 0, -1):
    rw = w + d
    small_adult_idx = bisect.bisect_left(adults, rw)
    cc_of_adults = len(adults) - small_adult_idx
    cc_of_children = bisect.bisect_left(children, rw)
    m = cc_of_adults + cc_of_children
    max_m = max(max_m, m)

print(max_m)