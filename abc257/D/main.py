#!/usr/bin/env python3.8
import math
from numpy import subtract, abs, minimum, maximum
N = int(input())
X = []
Y = []
P = []
for i in range(N):
  x, y, p = map(int, input().split())
  X.append(x)
  Y.append(y)
  P.append(p)

f = lambda x: abs(subtract.outer(x, x))
d = (f(X) + f(Y)) / P
for k in range(N):
  cross = maximum.outer(d[:, k], d[k])
  d = minimum(d, cross)

ma = d.max(axis=0)
print(math.ceil(ma.min()))
