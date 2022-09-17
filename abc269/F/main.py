#!/usr/bin/env python3
N, M = map(int, input().split())
Q = int(input())

S = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  S.append((a, b, c, d))

P = []
for i in range(N):
  p = []
  for j in range(M):
    if ((i + 1) + (j + 1)) % 2 == 1:
      p.append(0)
    else:
      p.append(i * M + j + 1)
  P.append(p)

for p in P:
  print(p)

for s in S:
  ans = 0
  a, b, c, d = s
  for i in range(a - 1, b):
    for j in range(c - 1, d):
      ans += P[i][j]
  print(ans)

