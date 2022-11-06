#!/usr/bin/env python3.8
from itertools import product
N = int(input())

p = set('357')

cnt = 0
for i in range(3, 10):
  for comb in product('357', repeat=i):
    y = ''.join(comb)
    if int(y) > N:
      print(cnt)
      exit()
    if p == set(y):
      cnt += 1

print(cnt)