#!/usr/bin/env python3.8
N,x=map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 1
tot = 0
for i in range(N - 1):
  if A[i] + A[i + 1] > x:
    rem = min(A[i + 1], A[i] + A[i + 1] - x)
    if A[i + 1] > 0:
      A[i + 1] -= rem
      tot += rem

    rem = A[i] + A[i + 1] - x
    tot += rem
    A[i] -= rem
  # print(A)
print(tot)