#!/usr/bin/env python3.8
from collections import deque


N, K = map(int, input().split())
S = input()

next_starts = deque()
l = 0
r = 0
zero_cnt = 0
ml = 0
while l < N:
  k = r
  while r < N:
    if zero_cnt == K:
      while r < N and S[r] != '0':
        k = r
        r += 1
      break
      

    if S[r] == '1':
      k = r
      r += 1
      continue

    if S[r] == '0':
      zero_cnt += 1
      while r < N and S[r] == '0':
        k = r
        r += 1
      next_starts.append(r)

  r = k
  ml = max(ml, r - l + 1)
  if len(next_starts):
    l = next_starts.popleft()
    zero_cnt -= 1
  else:
    if l == r:
      r += 1
    l += 1
print(ml)