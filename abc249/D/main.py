#!/usr/bin/env python3
import math
N = int(input())
A = list(map(int, input().split()))

m = max(A)
P = [0] * (m + 1)

for i in range(N):
  P[A[i]] += 1
# 
# print(list(range(max(A) + 1)))
# print(P)

tot = 0
for j in range(1, m + 1):
  c = 0
  for i in range(j, m + 1, j):
    cnt = P[i]
    if cnt == 0:
      continue

    k = i // j
    p = cnt * P[j] * P[k]
    c += p

  tot += c

print(tot)