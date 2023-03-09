#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

A.sort()
counter = [0] * (max(A) + 1)
for i in range(N):
  counter[A[i]] += 1

tot = 0
two_cnt = 0
for j in range(max(A) + 1):
  if counter[j] == 0:
    counter[j] = 0
  elif counter[j] % 2 == 0:
    counter[j] = 2
    two_cnt += 1
  elif counter[j] % 2 != 0:
    counter[j] = 0
    tot += 1

tot += (two_cnt // 2) * 2
print(tot)