#!/usr/bin/env python3.8
L, H = map(int, input().split())
N = int(input())

for i in range(N):
  x = int(input())
  if x < L:
    print(L - x)
  elif H < x:
    print(-1)
  else:
    print(0)