#!/usr/bin/env python3.8
from collections import defaultdict
import sys
sys.setrecursionlimit(300000) 


N = int(input())
G = defaultdict(list)
for i in range(N - 1):
  num = i + 2
  b = int(input())
  G[b].append(num)


# print(G)

salaries = [None] * (2 + N)

def dfs(s):
  if len(G[s]) == 0:
    salaries[s] = 1
    return

  max_s = 0
  min_s = 1e18
  if len(G[s]) == 0:
    min_s = 0

  for child in G[s]:
    dfs(child)
    max_s = max(max_s, salaries[child])
    min_s = min(min_s, salaries[child])

  salaries[s] = max_s + min_s + 1

dfs(1)

# print(salaries)
print(salaries[1])