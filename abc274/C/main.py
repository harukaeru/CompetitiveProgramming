#!/usr/bin/env python3
from collections import defaultdict, deque
N = int(input())
A = list(map(int, input().split()))

G = defaultdict(list)

for i in range(N):
  a = A[i]
  G[a].append(2 * (i + 1))
  G[a].append(2 * (i + 1) + 1)

q = deque()
q.append(1)
dists = [-1] * (2 * N + 1)
dists[0] = 0

# print(G)
while len(q) > 0:
  x = q.popleft()
  for n in G[x]:
    if dists[n - 1] == -1:
      dists[n - 1] = dists[x - 1] + 1
      q.append(n)

for d in dists:
  print(d)