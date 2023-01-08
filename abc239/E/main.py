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
  graph[a].append(b)
  graph[b].append(a)

# 最初に取得しておいてあとからクエリを取る
queries = []
for i in range(Q):
  v,k = map(int, input().split())
  queries.append((v, k))

class Node:
  def __init__(self, parentNode, num, strength):
    self.parentNode = parentNode
    self.num = num
    self.strength = strength
    self.children = []
  
  def __repr__(self):
    return f'<cur: {self.num} | parent: {self.parentNode.num if self.parentNode else "None"}>'
  
  def decide_strength_ranking(self, strength_ranking):
    self.strength_ranking = strength_ranking

# DFSの初期化
seen = set()
seen.add(1)
ranks = defaultdict(list)

# Node周りの設定
startingNode = Node(None, 1, X[0])
ranks[0].append(startingNode)
cached_nodes = [None] * N
cached_nodes[0] = startingNode

def dfs(v, depth=0):
  for nex in graph[v.num]:
    if nex not in seen:
      seen.add(nex)
      nexNode = Node(v, nex, X[nex - 1])
      v.children.append(nexNode)

      ranks[depth + 1].append(nexNode)
      cached_nodes[nex - 1] = nexNode

      dfs(nexNode, depth=depth+1)

dfs(startingNode)

# 各ノードについてランキングを作成する。RMQ風味。
keys = list(ranks.keys())
max_rank = max(keys)
for k in range(max_rank, -1, -1):
  for node in ranks[k]:
    new_ranking = []
    for child in node.children:
      new_ranking += child.strength_ranking[:]
    new_ranking += [node.strength]
    new_ranking.sort(reverse=True)
    new_ranking = new_ranking[:STRENGTH_RANKING_LIMIT]

    node.decide_strength_ranking(new_ranking)


# for i in range(N):
#   print(cached_nodes[i].array)

for query in queries:
  v, k = query
  print(cached_nodes[v - 1].strength_ranking[k - 1])