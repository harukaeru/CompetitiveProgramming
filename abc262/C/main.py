#!/usr/bin/env python3
import math
N = int(input())
A = list(map(int, input().split()))

B = [0] * N
for i in range(N):
  if A[i] == i + 1:
    B[i] += 1

cnt = 0
for i in range(N):
  j = A[i] - 1
  if A[j] == i + 1 and i < j:
    cnt += 1

print(math.comb(sum(B), 2) + cnt)