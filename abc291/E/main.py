#!/usr/bin/env python3.8
from collections import defaultdict, deque

N,M=map(int, input().split())

G = defaultdict(set)
F = defaultdict(set)
for i in range(M):
  x,y = map(int, input().split())
  x -= 1
  y -= 1

  G[x].add(y)
  F[y].add(x)

L = []
initial_candidate = [y for y in range(N) if len(F.get(y, set())) == 0]
S = deque(initial_candidate)

while S:
  if len(S) > 1:
    print('No')
    exit()

  n = S.popleft()
  L.append(n)

  for m in G[n]:
    F[m].remove(n)
    if not F.get(m):
      S.append(m)
  G[n] = {}

has_edge = any([len(v) for v in G.values()])
if has_edge:
  print('No')
  exit()

seeds = [i + 1 for i in L]
anses = [None] * N
for i, seed in enumerate(seeds):
  anses[seed - 1] = i
print('Yes')
print(*[a + 1 for a in anses])
