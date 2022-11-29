#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
  B.append((A[i], i))

B.sort(reverse=True)

for i in range(N):
  print(B[i][1] + 1)