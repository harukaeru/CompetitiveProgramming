#!/usr/bin/env python3.8
from collections import defaultdict, deque

V,E=map(int, input().split())

G = defaultdict(set)
F = defaultdict(set)
for i in range(E):
  s,t = map(int, input().split())

  G[s].add(t)
  F[t].add(s)

L = []
S = [x for x in range(V) if len(F.get(x, set())) == 0]

while S:
  v = S.pop()
  L.append(v)
  for nex in G[v]:
    F[nex].remove(v)
    if not F[nex]:
      S.append(nex)

for l in L:
  print(l)