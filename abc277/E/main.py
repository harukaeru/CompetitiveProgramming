#!/usr/bin/env python3.8
from collections import defaultdict, deque

P = 3 * (10 ** 5)
N, M, K = map(int, input().split())
G = defaultdict(list)
for i in range(M):
  u,v,a = map(int, input().split())
  if a == 0:
    G[P + u].append(P + v)
    G[P + v].append(P + u)
  else:
    G[u].append(v)
    G[v].append(u)

S = list(map(int, input().split()))
for i in range(K):
  s = S[i]
  G[s].append(P + s)
  G[P + s].append(s)

# print(G)

dists = dict()
dists[1] = 0
q = deque()
q.append(1)

INF = 99999999999999

while q:
  v = q.popleft()
  for nex in G[v]:
    if dists.get(nex) is None:
      if v % P == nex % P:
        dists[nex] = dists[v]
        q.appendleft(nex)
      else:
        dists[nex] = dists[v] + 1
        q.append(nex)

x = min(dists.get(N % P, INF), dists.get(N % P + P, INF))
if x == INF:
  print(-1)
else:
  print(x)