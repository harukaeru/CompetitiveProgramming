#!/usr/bin/env python3.8
import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(sorted(set(A)))

counter = [0] * N
for i in range(N):
  pos = bisect.bisect_right(B, A[i])
  cnt = len(B) - pos
  counter[cnt] += 1

for c in counter:
  print(c)