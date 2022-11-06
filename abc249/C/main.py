#!/usr/bin/env python3.8
from collections import defaultdict
N, K = map(int, input().split())
S = []
for i in range(N):
  S.append(input())

def count(strs):
  counter = defaultdict(int)
  for s in strs:
    for l in set(s):
      counter[l] += 1
  type_cnt = 0
  for v in counter.values():
    if v == K:
      type_cnt += 1
  return type_cnt
    

max_count = 0
for i in range(2 ** N):
  p = i
  strs = []
  for k in range(N):
    if p % 2:
      strs.append(S[k])
    p //= 2
  max_count = max(max_count, count(strs))

print(max_count) 