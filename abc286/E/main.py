#!/usr/bin/env pypy3
import collections
from collections import defaultdict, deque

N = int(input())
A = list(map(int, input().split()))
S = []
for i in range(N):
  S.append(input())

G = collections.defaultdict(list)
edges = []
for i in range(N):
  for j in range(N):
    if S[i][j] == 'Y':
      G[i].append(j)
      edges.append((i, j, 1, A[j]))

cache = {}
def bfs(s, e):
    if cache.get((s, e)):
      return cache[(s, e)]
    d = [1e18]*N # 各頂点への最小コスト
    q = deque()
    q.append(s)
    d[s] = 0 # 自身への距離は0
    p = [0] * N
    m_cnt = 1e18
    point = -1
    while len(q) > 0:
      v = q.popleft()
      for nex in G[v]:
        if nex == e:
          reach_cnt = d[v] + 1
          if reach_cnt <= m_cnt:
            m_cnt = reach_cnt 
            point = max(point, p[v] + A[nex])
          d[nex] = d[v] + 1
          p[nex] = p[v] + A[nex]
          continue
        elif d[nex] == 1e18:
          d[nex] = d[v] + 1
          p[nex] = p[v] + A[nex]
          q.append(nex)
    cache[(s, e)] = m_cnt, point
    return m_cnt, point

Q = int(input())
for i in range(Q):
  u,v = map(int, input().split())
  u-= 1
  v -= 1

  x, y = bfs(u, v)
  if x == 1e18:
    print('Impossible')
    continue
  print(x, A[u] + y)