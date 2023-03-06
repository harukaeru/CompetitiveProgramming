#!/usr/bin/env pypy3
from collections import defaultdict, deque


N,M=map(int, input().split())

G = defaultdict(set)
for i in range(M):
  u,v=map(int, input().split())
  u-=1
  v-=1
  G[u].add(v)

cnt = 0
for i in range(N):
  seen = set()
  seen.add(i)

  q = deque()
  q.append(i)
  while q:
    v = q.popleft()

    for nex in G[v]:
      if nex in seen:
        continue
      seen.add(nex)
      q.append(nex)
      cnt += 1
print(cnt - M)