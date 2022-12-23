#!/usr/bin/env pypy3
from collections import defaultdict
import heapq


N, M = map(int, input().split())
A = list(map(int, input().split()))

G = defaultdict(set)
for i in range(M):
  u,v = map(int, input().split())
  u -= 1
  v -= 1
  G[u].add(v)
  G[v].add(u)

costs = []
controller = {}
for i in range(N):
  cost = sum([A[n] for n in G[i]])
  controller[i] = (cost, i)
  costs.append(controller[i])

# print(G)
heapq.heapify(costs)
# print(costs)

max_c = 0
done = set()
while len(costs) > 0:
  # print(costs)
  m = heapq.heappop(costs)
  cost, i = m
  if i in done:
    continue

  # print('i -->', i)
  # print('G[i]', G[i])
  for n in G[i]:
    # print('G[n]', G[n])
    G[n].remove(i)
    controller[n] = (controller[n][0] - A[i], n)
    heapq.heappush(costs, controller[n])
  max_c = max(max_c, cost)
  done.add(i)

print(max_c)