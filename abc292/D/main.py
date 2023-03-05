#!/usr/bin/env python3.8
from collections import defaultdict, deque


N,M=map(int, input().split())
G = defaultdict(list)
for i in range(M):
  u,v=map(int, input().split())
  u -= 1
  v -= 1
  if u == v:
    G[u].append(v)
  else:
    G[u].append(v)
    G[v].append(u)


seen = set()
for i in range(N):
  if i in seen:
    continue

  q = deque()
  q.append(i)
  v_counter = 0
  e_counter = 0

  while q:
    v = q.popleft()
    if v in seen:
      continue
    v_counter += 1

    for nex in G[v]:
      if nex not in seen:
        e_counter += 1
        q.append(nex)
    seen.add(v)
  if v_counter != e_counter:
    print('No')
    exit()
  # print(v_counter, e_counter)
print('Yes')