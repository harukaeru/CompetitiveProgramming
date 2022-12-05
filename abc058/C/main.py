#!/usr/bin/env python3.8
import string
from collections import Counter

N = int(input())
S = []
for i in range(N):
  S.append(input())


tot = Counter(S[0])
for i in range(1, N):
  s = S[i]
  counter = Counter(s)
  for k, v in tot.items():
    tot[k] = min(tot[k], counter.get(k, 0))

s = ''
for k in string.ascii_lowercase:
  s += k * tot[k]
print(s)