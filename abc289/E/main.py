#!/usr/bin/env python3.8
from collections import defaultdict, deque

T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  C = list(map(int, input().split()))
  blues = set()
  reds = set()
  for i in range(N):
    if C[i]:
      blues.add(i)
    else:
      reds.add(i)

  G = defaultdict(list)
  for i in range(M):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    G[v].append(u)
    G[u].append(v)
  
  dists = []
  for i in range(N):
    dists.append([1e10] * N)
  s = (0, N - 1)
  dists[0][N-1] = 0
  q = deque()
  q.append(s)
  while len(q) > 0:
    orig_key = q.popleft()
    t_v, a_v = orig_key

    for t_nex in G[t_v]:
      for a_nex in G[a_v]:
        if C[t_nex] == C[a_nex]:
          continue
        key = (t_nex, a_nex)
        if dists[t_nex][a_nex] == 1e10:
          dists[t_nex][a_nex] = dists[t_v][a_v] + 1
          q.append(key)
  if dists[N - 1][0] != 1e10:
    print(dists[N - 1][0])
  else:
    print(-1)
  
  
  