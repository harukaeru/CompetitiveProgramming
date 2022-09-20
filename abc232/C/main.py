#!/usr/bin/env python3
from itertools import permutations
from collections import defaultdict

def get_graph(seeds):
  B = defaultdict(list)
  for x, y in seeds:
    B[x].append(y)
    B[y].append(x)
  for value in B.values():
    value.sort()
  return B

N, M = map(int, input().split())

first = []
for i in range(M):
  x, y = map(int, input().split())
  first.append((x, y))

second = []
for i in range(M):
  x, y = map(int, input().split())
  second.append((x, y))

A = get_graph(first)

seeds = list(range(1, N + 1))
for converter in permutations(seeds):
  second2 = []
  for x, y in second:
    x2 = converter[x - 1]
    y2 = converter[y - 1]
    second2.append((x2, y2))
  B = get_graph(second2)
  if A == B:
    print('Yes')
    exit()

print('No')