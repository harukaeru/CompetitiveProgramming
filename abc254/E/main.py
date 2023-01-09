#!/usr/bin/env python3.8
from collections import defaultdict, deque
import itertools

N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
  a,b=map(int, input().split())
  a-=1
  b-=1
  G[a].append(b)
  G[b].append(a)

dp = []
for i in range(N):
  dp.append([0 for j in range(4)])

for i in range(N):
  seen = set()
  q = deque()
  q.append((i, 0))
  dp[i][0] += (i + 1)
  seen.add(i)

  while len(q) > 0:
    v, dist = q.popleft()
    for nex in G[v]:
      if nex not in seen:
        seen.add(nex)
        if dist + 1 < 4:
          q.append((nex, dist + 1))
          dp[i][dist + 1] += (nex + 1)

B = []
for d in dp:
  b = list(itertools.accumulate(d))
  B.append(b)
  # print(b)
Q = int(input())

for i in range(Q):
  x,k = map(int, input().split())
  x -= 1
  print(B[x][k])
  

