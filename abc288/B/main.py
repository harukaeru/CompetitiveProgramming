#!/usr/bin/env python3.8
N,K=map(int, input().split())
S = []
for i in range(K):
  S.append(input())

S.sort()

for s in S:
  print(s)
  