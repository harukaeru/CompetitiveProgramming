#!/usr/bin/env python3
import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))

A = [-a for a in A]
heapq.heapify(A)

for i in range(M):
  a = heapq.heappop(A)
  # print('a', -a)
  b = -a // 2
  heapq.heappush(A, -b)


print(-sum(A))