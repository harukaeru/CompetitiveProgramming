#!/usr/bin/env python3.8
from collections import Counter


H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

T = []
for i in range(H):
  T.append(input())


NS = []
for j in range(W):
  x = ''
  for i in range(H):
    x += S[i][j]
  NS.append(x)

NT = []
for j in range(W):
  x = ''
  for i in range(H):
    x += T[i][j]
  NT.append(x)


sc = Counter(NS)
tc = Counter(NT)
if sc == tc:
  print('Yes')
else:
  print('No')