#!/usr/bin/env python3.8
N,M= map(int, input().split())

edges = []
for i in range(M):
  a,b,c = map(int, input().split())
  a-=1
  b-=1
  edges.append((a, b, c))
  # costs[a][b] = c

dists = []
for i in range(N):
  d = []
  for j in range(N):
    if i == j:
      d.append(0)
    else:
      d.append(1e10)
  dists.append(d)
for edge in edges:
  a,b,c = edge
  dists[a][b] = c

ans = 0
for k in range(N):
  for i in range(N):
    for j in range(N):
      dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

  for i in range(N):
    for j in range(N):
      v = dists[i][j]
      if v == 1e10:
        continue
      ans += v
print(ans)