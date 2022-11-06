#!/usr/bin/env python3.8
from queue import Queue
from collections import defaultdict
N, X, Y = map(int, input().split())
G = defaultdict(list)
for i in range(N - 1):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)

q = Queue()
q.put(X - 1)
dist = [-1] * N
dist[X - 1] = 0
parents = [None] * N
parents[X - 1] = -1

while q.qsize() > 0:
  x = q.get()
  for p in G.get(x, []):
    if dist[p] == -1:
      dist[p] = dist[x] + 1
      parents[p] = x
      q.put(p)

y = Y - 1
ans = []
while y != -1:
  ans.append(y + 1)
  y = parents[y]
ans.reverse()
print(*ans)