#!/usr/bin/env python3.8
import itertools


N = int(input())
A = list(map(int, input().split()))

r = 0
cur = 0
ans = 0
for l in range(N):
  while r < N and (cur ^ A[r]) == (cur + A[r]):
    cur ^= A[r]
    r += 1

  # print(r - l)
  ans += r - l
  
  # print('(l,r)', l, r, '->', cur)
  if l == r:
    r += 1
  cur ^= A[l]

print(ans)