#!/usr/bin/env python3.8
import bisect


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

counts = [0] * N
for i in range(N):
  idx = bisect.bisect_left(A, B[i])
  counts[i] = idx

for i in range(N):
  idx = bisect.bisect_right(C, B[i])
  counts[i] *= (N - idx)

print(sum(counts))