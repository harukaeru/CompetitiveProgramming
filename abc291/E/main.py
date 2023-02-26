#!/usr/bin/env python3.8
from collections import defaultdict

N,M=map(int, input().split())

G = defaultdict(list)
for i in range(M):
  x,y = map(int, input().split())
  x -= 1
  y -= 1

  G[x].append(y)

current = []
seen = set()
def dfs(v):
  current.append(v)
  if len(current) == N:
    print('Yes')
    # print('current', *[x + 1 for x in current])
    ans = [None] * N
    for i in range(N - 1, -1, -1):
      # print('i', i)
      # print('current[i]', current[i])
      ans[current[i]] = i + 1
      # print(ans)
    print(*ans)
    exit()

  for nex in G[v]:
    if nex not in seen:
      seen.add(nex)
      dfs(nex)
      current.pop()


ultraseen = set()
for i in range(N):
  if i in ultraseen:
    continue

  seen = set()
  seen.add(i)
  current = []

  dfs(i)

  ultraseen = ultraseen.union(seen)

print('No')