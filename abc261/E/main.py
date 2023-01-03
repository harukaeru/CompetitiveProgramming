#!/usr/bin/env pypy3
N,C=map(int, input().split())
A = []
for i in range(N):
  t, a = map(int, input().split())
  A.append((t, a))

M = 30

dp = []
for i in range(N + 1):
  d = []
  for j in range(M):
    if i == 0:
      dd = [0, 1]
    else:
      dd = None
    d.append(dd)
  dp.append(d)

for i in range(N):
  pattern, a = A[i]
  b = a
  dd = dp[i]
  if pattern == 1:
    for d in range(M):
      c = b & (1 << d) != 0

      k = dd[d]
      dp[i + 1][d] = [c & k[0], c & k[1]]
  elif pattern == 2:
    for d in range(M):
      c = b & (1 << d) != 0

      k = dd[d]
      dp[i + 1][d] = [c | k[0], c | k[1]]
  else:
    for d in range(M):
      c = b & (1 << d) != 0

      k = dd[d]
      dp[i + 1][d] = [c ^ k[0], c ^ k[1]]

c = C
cache = [2 ** i for i in range(M)]
for i in range(1, N + 1):
  s = 0
  d = dp[i]
  for j in range(M):
    v = (c & (1 << j)) != 0
    # print(v, end='')
    if d[j][v]:
      s += cache[j]

  c = s
  # c = int(s, 2)
  print(c)