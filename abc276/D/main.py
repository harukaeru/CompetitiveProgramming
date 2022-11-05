#!/usr/bin/env python3
import math
N = int(input())
A = list(map(int, input().split()))

K = []
C2 = []
C3 = []

for i in range(N):
  a = A[i]

  k = a
  c2 = 0
  while k % 2 == 0:
    k //= 2
    c2 += 1

  c3 = 0
  while k % 3 == 0:
    k //= 3
    c3 += 1
  K.append(k)
  C2.append(c2)
  C3.append(c3)

if N != K.count(K[0]):
  print(-1)
  exit()

mc2 = min(C2)
for i in range(N):
  C2[i] -= mc2
mc3 = min(C3)
for i in range(N):
  C3[i] -= mc3

print(sum(C2) + sum(C3))