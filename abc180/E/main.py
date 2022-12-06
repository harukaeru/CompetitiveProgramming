#!/usr/bin/env pypy3
N = int(input())
P = []
for i in range(N):
  x,y,z= map(int, input().split())
  P.append((x, y, z))

dists = [1e18 for i in range(2 ** N)]

dp = []
for i in range(1 << N):
  d = [1e18] * (N)
  dp.append(d)
dp[1][0] = 0

def hypot(a, b):
  return abs(b[0] - a[0]) + abs(b[1] - a[1]) + max(0, b[2] - a[2])

# 集合sについて
for s in range(1 << N):
  # 現在都市iからjに移動する
  for i in range(N):
    for j in range(N):
      # 同じ都市の移動はスキップ
      if i == j:
        continue

      # すでに探索済みならスルー
      if s & (1 << j) != 0:
        continue

      dp[s | (1 << j)][j] = min(dp[s | (1 << j)][j], dp[s][i] + hypot(P[i], P[j]))

md = 1e18
for i, d in enumerate(dp[-1]):
  md = min(md, hypot(P[i], P[0]) + d)

print(md)