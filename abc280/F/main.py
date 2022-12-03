#!/usr/bin/env python3.8
from collections import defaultdict


N, M, Q = map(int, input().split())
G = defaultdict(list)
scores = dict()
for i in range(M):
  a,b,c= map(int, input().split())
  G[a].append(b)
  G[b].append(a)
  scores[(a, b)] = c
  scores[(b, a)] = -c

for i in range(Q):
  x,y= map(int, input().split())
