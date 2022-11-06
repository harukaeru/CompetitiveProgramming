#!/usr/bin/env python3.8
N, M = map(int, input().split())
S = input().split()
T = input().split()

T = set(T)

for s in S:
  if s in T:
    print('Yes')
  else:
    print('No')