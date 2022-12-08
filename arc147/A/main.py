#!/usr/bin/env pypy3
import heapq

N = int(input())
A = list(map(int, input().split()))

B = [-a for a in A]
heapq.heapify(A)
heapq.heapify(B)

ignore_set = set()

i = 0
while True:
  try:
    small = A[0]
    big = heapq.heappop(B)
  except:
    print(i - 1)
    exit()

  i += 1
  newbig = -big % small
  if newbig != 0:
    heapq.heappush(A, newbig)
    heapq.heappush(B, -newbig)
