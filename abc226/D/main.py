#!/usr/bin/env python3.8
import math


N = int(input())
coods = []
for i in range(N):
  x, y  = map(int, input().split())
  coods.append((x, y))

def dir(a, b):
  return (a[0] - b[0], a[1] - b[1])

ts = []
for i in range(N - 1):
  for j in range(i + 1, N):
    t1 = dir(coods[i], coods[j])
    t2 = dir(coods[j], coods[i])
    m1 = math.gcd(t1[0], t1[1])
    m2 = math.gcd(t2[0], t2[1])
    ts.append((t1[0] // m1, t1[1] // m1))
    ts.append((t2[0] // m2, t2[1] // m2))

ts = set(ts)
# ts = list(set(ts))
# ts.sort()
print(len(ts))