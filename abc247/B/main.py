#!/usr/bin/env python3
from collections import Counter
N = int(input())


counter = Counter()
names = []

for i in range(N):
  s, t = input().split()
  counter[s] += 1
  counter[t] += 1
  names.append((s, t))

for s, t in names:
  if s == t:
    if counter[s] > 2:
      print('No')
      exit()
  elif counter[s] > 1 and counter[t] > 1:
    print('No')
    exit()

print('Yes')