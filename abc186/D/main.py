#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

A.sort()

LS = [0] * (N + 1)
for i in range(1, N + 1):
  LS[i] = LS[i - 1] + A[i - 1]

s = 0
for i in range(1, N + 1):
  right_sum = LS[N] - LS[i]
  right = A[i - 1] * (N - i)
  x = right_sum - right

  s += x
print(s)