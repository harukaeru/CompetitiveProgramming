#!/usr/bin/env pypy3
from collections import Counter, deque


H,W=map(int, input().split())
A = []
B = []
for i in range(H):
  a = list(map(int, input().split()))
  A.append(a)
  B += a

B = list(set(B))
B.sort()
convs = {}
for i in range(len(B)):
  convs[B[i]] = i

for i in range(H):
  for j in range(W):
    A[i][j] = convs[A[i][j]]

dp = []
for i in range(H):
  d = [Counter() for j in range(W)]
  dp.append(d)

seen = set()
q = deque()
q.append((0, 0))
dp[0][0][(1 << A[0][0])] = 1

while q:
  y, x = q.popleft()
  if (y, x) in seen:
    continue
  for dy, dx in [(1, 0), (0, 1)]:
    ny = y + dy 
    nx = x + dx 
    if not (0 <= ny < H and 0 <= nx < W):
      continue

    for s, cnt in dp[y][x].items():
      if s & (1 << A[ny][nx]) == 0:
        dp[ny][nx][s | (1 << A[ny][nx])] += dp[y][x][s]
    q.append((ny, nx))
  seen.add((y, x))

print(sum(dp[H - 1][W - 1].values()))
# for d in dp:
#   print(d)