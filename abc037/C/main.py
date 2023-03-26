#!/usr/bin/env python3.8
import itertools


N,K=map(int, input().split())
A = list(map(int, input().split()))

C = [0] * (N + 1)

for i in range(N - K + 1):
  C[i] += 1
  C[i + K] -= 1

B = list(itertools.accumulate(C))
# print(B)

tot = 0
for i in range(N):
  tot += A[i] * B[i]
print(tot)