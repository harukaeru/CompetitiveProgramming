#!/usr/bin/env python3.8
N = int(input())
S = list(map(int, input().split()))

f = 0
A = []
for i in range(N):
  x = S[i] - f
  A.append(x)
  f += x
print(*A)