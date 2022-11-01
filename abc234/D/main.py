#!/usr/bin/env pypy3
import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))

Q = P[:K]

heapq.heapify(Q)
print(min(Q))

for i in range(K, N):
  minimax = heapq.heappop(Q)
  minimax = max(minimax, P[i])
  heapq.heappush(Q, minimax)

  ans = heapq.heappop(Q)
  print(ans)
  heapq.heappush(Q, ans)