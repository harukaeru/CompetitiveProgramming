#!/usr/bin/env python3.8
import bisect
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())


xlist = defaultdict(list)
for i in range(N):
  xlist[A[i]].append(i + 1)

for v in xlist.values():
  v.sort()

# print(xlist)

for q in range(Q):
  L, R, X = map(int, input().split())
  l = bisect.bisect_left(xlist[X], L)
  r = bisect.bisect_right(xlist[X], R)
  print(r - l)