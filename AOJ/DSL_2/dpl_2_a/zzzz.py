#!/usr/bin/env python3.8
from itertools import permutations
from collections import defaultdict
V, E = map(int, input().split())

LIM = 9999999999

G = defaultdict(dict)
for i in range(E):
  s, t, d = map(int, input().split())
  G[s][t] = min(G[s].get(t, LIM), d)

min_d = LIM
for perm in permutations(range(V)):
  tot_d = 0
  cut = False
  # print('------', perm)
  for i in range(len(perm)):
    pp = perm[i]
    pn = perm[(i + 1) % len(perm)]
    if G.get(pp) is None or G[pp].get(pn) is None:
      cut = True
      break

    # print('i', pp, '=>', pn)
    tot_d += G[pp][pn]
  if cut:
    continue
  min_d = min(min_d, tot_d)

if min_d == LIM:
  print(-1)
else:
  print(min_d)