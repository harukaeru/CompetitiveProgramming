#!/usr/bin/env python3.8
import itertools


N,M,R = map(int, input().split())
rs = list(map(int, input().split()))
dists = []
for i in range(N):
  dists.append([1e10] * N)

for i in range(M):
  a,b,c=map(int, input().split())
  a-=1
  b-=1
  dists[a][b] = c
  dists[b][a] = c

for k in range(N):
  for i in range(N):
    for j in range(N):
      dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

rs = [r - 1 for r in rs]
md = 1e18
for ss in itertools.permutations(rs):
  d = 0
  for i in range(len(ss) - 1):
    d += dists[ss[i]][ss[i + 1]]
  md = min(md, d)
print(md)