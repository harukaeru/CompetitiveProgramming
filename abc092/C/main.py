#!/usr/bin/env python3
N = int(input())
A = [0] + list(map(int, input().split())) + [0]

total_d = 0
flg_array = []
for i in range(len(A) - 1):
  total_d += abs(A[i + 1] - A[i])

d1_array = []
for i in range(N + 1):
  d1_array.append(abs(A[i + 1] - A[i]))

d2_array = []
for i in range(N):
  d2_array.append(abs(A[i + 2] - A[i]))


for i in range(N):
  ans = total_d - (d1_array[i] + d1_array[i + 1]) + d2_array[i]
  print(ans)