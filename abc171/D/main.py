#!/usr/bin/env python3.8
from collections import Counter


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

counter = Counter(A)

s = 0
for k,v in counter.items():
  s += k * v
for i in range(Q):
  b,c=map(int,input().split())
  cnt = counter[b]
  counter[b] = 0
  counter[c] += cnt
  s -= b * cnt
  s += c * cnt

  print(s)