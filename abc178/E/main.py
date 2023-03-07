#!/usr/bin/env python3.8
N = int(input())
Z = []
W = []
for i in range(N):
  x, y = map(int, input().split())
  Z.append(x + y)
  W.append(x - y)

print(max(max(Z) - min(Z), max(W) - min(W)))