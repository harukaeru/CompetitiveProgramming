#!/usr/bin/env python3.8
from collections import defaultdict


N,M=map(int, input().split())
if M == 0:
  print(*list(range(1, N + 1)))
  exit()
A = list(map(int, input().split()))
G = defaultdict(list)

for a in A:
  G[a].append(a + 1)

ans = []
seen = set()
def add(i):
  for nex in G[i]:
    if nex not in seen:
      add(nex)

  if i not in seen:
    ans.append(i)
  seen.add(i)


for i in range(1, N + 1):
  add(i)

print(*ans)