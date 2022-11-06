#!/usr/bin/env python3.8
from collections import defaultdict


K = int(input())

G = {}
for k in range(10):
  G[k] = defaultdict(list)

for i in range(1, 10):
  for j in range(1, 10):
    p = (i * j) % 10
    G[p][i].append(j)

print(G)

sk = list(map(int, str(K)))
sk.reverse()

print('K', K)
m = 99999999
def dfs(res, depth, ans):
  global m
  if len(sk) == depth:
    m = min(m, ans)
    return
  rs = G[res].get(sk[depth])
  if rs is None:
    return

  for r in rs:
    print('  ' * depth + 'r', sk[depth], 'x', r, '=>', res)

    for i in range(10):
      r2 = (i * 10 + r)
      nex = (K * r2 % 100) // 10
      print('  ' * (depth + 1) + 'x', r2, '=>', K * r2)
      dfs(nex, depth + 1, ans + nex)


for i in range(10):
  dfs(i, 0, i)
print('m', m)