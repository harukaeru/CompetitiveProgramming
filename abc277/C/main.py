#!/usr/bin/env python3.8
from collections import defaultdict, deque
N = int(input())
G = defaultdict(list)
for i in range(N):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

seen = set()
q = deque()
q.append(1)
seen.add(1)

m = 1
while len(q) > 0:
  x = q.popleft()

  for nex in G[x]:
    if nex in seen:
      continue
    m = max(m, nex)
    seen.add(nex)
    q.append(nex)
print(m)
