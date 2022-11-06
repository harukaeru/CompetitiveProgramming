#!/usr/bin/env python3.8
T = int(input())
N = int(input())

P = [0] * (T + 1)
for i in range(N):
  l, r = map(int, input().split())
  P[l] += 1
  P[r] -= 1

sp = [0] * (T + 2)
for i, p in enumerate(P):
  sp[i + 1] = sp[i] + p

for s in sp[1:T + 1]:
  print(s)