#!/usr/bin/env python3.8
from collections import Counter


N, K = map(int, input().split())
counter = Counter()
t = 0
for i in range(N):
  a,b=map(int,input().split())
  t = max(t, a)
  counter[a] += b

# print(counter)
cnt = 0
for i in range(1, t + 1):
  cnt += counter[i]
  if cnt >= K:
    print(i)
    exit()