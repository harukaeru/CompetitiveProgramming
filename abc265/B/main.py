#!/usr/bin/env python3.8
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [0] * N
for i in range(M):
  x, y = map(int, input().split())
  XY[x - 1] += y

for i in range(N - 1):
  T -= A[i]
  if T <= 0:
    print('No')
    exit()
  T += XY[i + 1]

print('Yes')
