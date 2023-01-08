#!/usr/bin/env python3.8
import sys
from collections import defaultdict
sys.setrecursionlimit(300000) 
STRENGTH_RANKING_LIMIT = 20

N, Q = map(int, input().split())
X = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(N - 1):
  a,b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a].append(b)
  graph[b].append(a)

# 最初に取得しておいてあとからクエリを取る
queries = []
for i in range(Q):
  v,k = map(int, input().split())
  queries.append((v, k))

weights_list = [[] for i in range(N)]

# DFSの初期化
seen = set()
seen.add(0)

def dfs(v):
  weights_list[v] += [X[v]]
  for nex in graph[v]:
    if nex not in seen:
      seen.add(nex)
      dfs(nex)
      weights_list[v] += weights_list[nex]
  weights_list[v] = sorted(weights_list[v], reverse=True)[:STRENGTH_RANKING_LIMIT]

dfs(0)

for query in queries:
  v, k = query
  print(weights_list[v - 1][k - 1])