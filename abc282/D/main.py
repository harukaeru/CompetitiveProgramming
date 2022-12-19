#!/usr/bin/env pypy3
# https://note.nkmk.me/python-union-find/
from collections import Counter, defaultdict, deque
import itertools
N, M = map(int, input().split())

G = defaultdict(list)
node_counter = defaultdict(int)
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)
  node_counter[u] += 1
  node_counter[v] += 1

colors = [1e18] * N
groups = {}
for i in range(N):
  if colors[i] != 1e18:
    continue

  colors[i] = 0
  q = deque()
  q.append(i)
  gs = set()
  gs.add(i)

  while len(q) > 0:
    x = q.pop()
    for nex in G[x]:
      gs.add(nex)
      if colors[nex] == 1e18:
        colors[nex] = colors[x] ^ 1
        q.append(nex)
      else:
        if colors[nex] == colors[x]:
          print(0)
          exit()
  groups[i] = gs

ans = 0
for k, v in groups.items():
  counter = Counter([colors[vv] for vv in v])
  cnt = sum([node_counter[vv] for vv in v]) // 2
  tot = counter[0] * counter[1]
  ans += tot - cnt

lans = 0
values = [len(v) for v in groups.values()]
total = sum(values)

for i in range(len(values)):
  v = values[i]
  lans += v * (total - v)
ans += lans // 2
print(ans)