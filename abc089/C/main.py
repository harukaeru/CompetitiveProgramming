#!/usr/bin/env python3
from collections import Counter
N = int(input())

counter = Counter()
for i in range(N):
  data = input()
  v = data[0]
  if v in 'MARCH':
    counter[v] += 1

keys = 'MARCH'
l = len(keys)
total = 0
for i in range(l - 2):
  for j in range(i + 1, l - 1):
    for k in range(j + 1, l):
      comb = counter[keys[i]] * counter[keys[j]] * counter[keys[k]]
      total += comb

print(total)