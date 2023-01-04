#!/usr/bin/env python3.8
# https://note.nkmk.me/python-union-find/
from collections import defaultdict, deque
N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

G = defaultdict(list)
for i in range(N):
  a = i
  b = X[i]
  b -= 1
  G[a].append(b)
  # uf.union(a, b)

seen = set()
tot = 0
for i in range(N):
  if i in seen:
    continue

  q = deque()
  q.append(i)
  seen.add(i)
  cycle = []
  cycle.append(i)
  cycleset = set()
  cycleset.add(i)
  pos_cycle = {}
  pos_cycle[i] = 0

  is_cycle = False
  while len(q) > 0:
    v = q.popleft()
    for nex in G[v]:
      if nex in cycleset:
        is_cycle = True
        break
      if nex in seen:
        break
      seen.add(nex)
      pos_cycle[nex] = len(cycle)
      cycle.append(nex)
      cycleset.add(nex)
      q.append(nex)
  
  if is_cycle:
    j = pos_cycle[nex]
    cc = cycle[j:]
    tot += min([C[c] for c in cc]) if cc else 0
print(tot)