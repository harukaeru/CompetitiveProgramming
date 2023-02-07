#!/usr/bin/env python3.8
from collections import defaultdict
import math

def calc_dist(a, b):
  s = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
  return math.sqrt(s)

N = int(input())
G = defaultdict(list)
coords = []
for i in range(N):
  x, y = map(int, input().split())
  coords.append((x, y))

dists = []
for i in range(N):
  dists.append([1e18] * N)

for i in range(N):
  for j in range(N):
    dist = calc_dist(coords[i], coords[j])
    G[i + 1].append((dist, j + 1))
    G[j + 1].append((dist, i + 1))

dp = []
for i in range(2 ** N):
  d = [1e18] * (N + 1)
  dp.append(d)

dp[1][1] = 0

# 通ってきた都市
for i in range(1, 2 ** N):
  # 今いる都市
  for j in range(1, N + 1):
    for d, nex in G[j]:
      k = 1 << (nex - 1)
      dp[i | k][nex] = min(dp[i | k][nex], dp[i][j] + d)

# for i, d in enumerate(dp):
#   print(bin(i), d)

md = 1e18
for pos, dist in enumerate(dp[-1]):
  for d, destination in G[pos]:
    if destination == 1:
      md = min(md, dist + d)
      break

print(md)