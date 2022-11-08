#!/usr/bin/env python3.8
import heapq
N = int(input())
A = list(map(int, input().split()))

A.sort()
A.reverse()

ans = A[0]
pairs = [(-min(A[0], A[1]), A[0], A[1]), (-min(A[1], A[0]), A[1], A[0])]

for i in range(2, N):
  pair = heapq.heappop(pairs)
  ans += -pair[0]

  mm = pair[1]
  heapq.heappush(pairs, (-min(mm, A[i]), mm, A[i]))

  mi = pair[2]
  heapq.heappush(pairs, (-min(mi, A[i]), mi, A[i]))

print(ans)
# print(pairs)