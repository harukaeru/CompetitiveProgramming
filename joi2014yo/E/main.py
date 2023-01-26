#!/usr/bin/env python3.8
from collections import defaultdict, deque
import heapq

inf = 10 ** 10

N,K=map(int, input().split())
P = []
R = []
for i in range(N):
  p,r = map(int, input().split())
  P.append(p)
  R.append(r)

G = defaultdict(list)
for i in range(K):
  a,b=map(int, input().split())
  a-=1
  b-=1
  G[a].append(b)
  G[b].append(a)

def bfs(s):
  dists = [inf] * N
  dists[s] = 0
  q = deque()
  q.append(s)
  while q:
    v = q.popleft()
    for nex in G[v]:
      if dists[nex] == inf:
        dists[nex] = dists[v] + 1
        q.append(nex)
  return dists

dists_list = [bfs(i) for i in range(N)]

for i in range(N):
  for j in range(N):
    if dists_list[i][j] <= R[i]:
      dists_list[i][j] = P[i]
    else:
      dists_list[i][j] = inf

K = 10 ** 10
def pack(a, b):
  return a * K + b

def unpack(ab):
  return ab // K, ab % K

pq = [pack(0, 0)]
costs = [inf] * N
costs[0] = 0
while pq:
  c, v = unpack(heapq.heappop(pq))
  if costs[v] < c:
    continue
  if v == N - 1:
    break

  for nex in range(N):
    if v == nex:
      continue
    nc = dists_list[v][nex]
    nnc = c + nc
    if costs[nex] > nnc:
      costs[nex] = nnc
      heapq.heappush(pq, pack(nnc, nex))

print(costs[N - 1])