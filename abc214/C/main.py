#!/usr/bin/env python3.8
import heapq


N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

pq = []
for i, t in enumerate(T):
  heapq.heappush(pq, (t, i))

while pq:
  t, i = heapq.heappop(pq)
  if T[i] < t:
    continue

  nex = (i + 1) % N
  if T[nex] > S[i] + t:
    T[nex] = S[i] + t
    heapq.heappush(pq, (T[nex], nex))

for t in T:
  print(t)