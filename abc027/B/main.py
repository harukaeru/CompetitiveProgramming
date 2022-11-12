#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

tot = sum(A)
if tot % N != 0:
  print(-1)
  exit()

avg = tot // N

cnt = 0
for i in range(N - 1):
  if A[i] > avg:
    A[i + 1] += A[i] - avg
    cnt += 1
  elif A[i] < avg:
    A[i + 1] -= avg - A[i]
    cnt += 1
print(cnt)