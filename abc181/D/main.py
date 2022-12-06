#!/usr/bin/env python3.8
from collections import Counter

S = input()
counter = Counter(S)

if len(S) <= 3:
  x = 0
  for i in range(10 ** 3):
    x += 8
    t = Counter(str(x))
    if counter == t:
      print('Yes')
      exit()
  print('No')
  exit()

eights = []
i = 96
while i <= 1000:
  i += 8
  eights.append(i)
for e in eights:
  c = Counter(str(e))
  if all([counter[ck] >= cv for ck, cv in c.items()]):
    print('Yes')
    exit()
print('No')