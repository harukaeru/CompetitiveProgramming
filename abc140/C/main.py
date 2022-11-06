#!/usr/bin/env python3.8
N = int(input())
B = list(map(int, input().split()))

A = [0] * N
A[0] = B[0]
for i in range(N - 2):
  A[i + 1] = min(B[i], B[i+1])
A[N - 1] = B[N - 2]

print(sum(A))