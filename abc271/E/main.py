#!/usr/bin/env python3.8
from queue import deque
from collections import defaultdict
N, M, K = map(int, input().split())
G = defaultdict(list)
dists = {}
A, B, C = []
for i in range(M):
  a, b, c = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  G[a].append(b)
  dists[(a, b)] = min(dists.get((a, b), 99999999999999), c)
E = list(map(int, input().split()))

q = deque()
q.append(1)

seen = set()

while len(q) > 0:
  a = q.popleft()
  seen.add(a)
  for b in G[a]:
    if b not in seen:
      d = dists[(a, b)]
      min_d = min(min_d, d)

    
