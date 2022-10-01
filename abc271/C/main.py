#!/usr/bin/env python3
from collections import Counter
N = int(input())
A = set(map(int, input().split()))

l = 0
r = N + 1
while r - l > 1:
  mid = (l + r) // 2
  c = len(set(range(1, mid + 1)) & A)
  if c + (N - c) // 2 >= mid:
    l = mid
  else:
    r = mid
  
print(l)