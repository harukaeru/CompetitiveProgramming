#!/usr/bin/env python3
N, M = map(int, input().split())
K = []
X = []

data = []
for i in range(N):
  d = []
  for j in range(N):
    if i == j:
      d.append(True)
    else:
      d.append(False)
  data.append(d)


for i in range(M):
  k, *x = map(int, input().split())
  for p in range(k - 1):
    for q in range(p + 1, k):
      data[x[p] - 1][x[q] - 1] = True
      data[x[q] - 1][x[p] - 1] = True

if all([all(d) for d in data]):
  print('Yes')
else:
  print('No')