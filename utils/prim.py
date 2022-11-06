#!/usr/bin/env python3.8
from collections import defaultdict
G = dict()

N = int(input())
V = set()
for i in range(N):
  a, b, c = map(int, input().split())
  G[(a, b)] = c
  G[(b, a)] = c
  V.add(a)
  V.add(b)

h = V.pop()
V.add(h)
H = set()
H.add(h)
M = set()

while H != V:
  min_c = 999999999999999
  min_h = None
  for u, v in G.keys():
    if u in H and v in (V - H):
      if min_c > G[(u, v)]:
        min_c = G[(u, v)]
        min_h = v
  M.add(min_c)
  print(min_h)
  H.add(min_h)

print(M)
print(H)