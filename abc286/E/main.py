#!/usr/bin/env pypy3
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
S = []
for i in range(N):
  S.append(input())

dists = []
for i in range(N):
  dists.append([1e18] * N)
vals = []
for i in range(N):
  vals.append([0] * N)

for i in range(N):
  for j in range(N):
    if S[i][j] == 'Y':
      dists[i][j] = 1
      vals[i][j] = A[j]
    else:
      vals[i][j] = A[j]

for i in range(N):
  for j in range(N):
    for k in range(N):
      if dists[j][k] > dists[j][i] + dists[i][k]:
        dists[j][k] = min(dists[j][k], dists[j][i] + dists[i][k])
        vals[j][k] = vals[j][i] + vals[i][k]
      elif dists[j][k] == dists[j][i] + dists[i][k] and vals[j][k] < vals[j][i] + vals[i][k]:
        vals[j][k] = vals[j][i] + vals[i][k]

Q = int(input())
for i in range(Q):
  u,v = map(int, input().split())
  u-= 1
  v -= 1

  d = dists[u][v]
  if d == 1e18:
    print('Impossible')
    continue
  print(d, vals[u][v] + A[u])