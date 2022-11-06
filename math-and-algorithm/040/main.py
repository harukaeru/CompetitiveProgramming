#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = []
for i in range(M):
  B.append(int(input()))

d = [0] * N
for i in range(1, N):
  d[i] = d[i - 1] + A[i - 1]

before = B[0]
s = 0
for current in B[1:]:
  s += d[max(current, before) - 1] - d[min(current, before) - 1]
  before = current

print(s)
  