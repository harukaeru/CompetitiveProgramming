#!/usr/bin/env pypy3
from collections import Counter, defaultdict, deque


N, X, Y = map(int, input().split())
G = defaultdict(list)
for i in range(N - 1):
  G[i].append(i + 1)
  G[i + 1].append(i)
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)

counter = Counter()
for i in range(N):
  q = deque()
  dists = [None] * N
  dists[i] = 0
  q.append(i)
  while q:
    v = q.popleft()
    for n in G[v]:
      if dists[n] is not None:
        continue
      dists[n] = dists[v] + 1
      q.append(n)
  counter += Counter(dists)
  # print(counter)

for i in range(1, N):
  print(counter[i] // 2)