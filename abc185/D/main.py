#!/usr/bin/env python3.8
N, M = map(int, input().split())
if M:
  A = list(map(int, input().split()))
else:
  A = []

A.append(0)
A.append(N + 1)
A.sort()

B = []
for i in range(len(A) - 1):
  d = A[i + 1] - A[i] - 1
  if d != 0:
    B.append(d)

if not B:
  print(0)
  exit()
m = min(B)
cnt = 0
for b in B:
  cnt += (b + m - 1) // m
print(cnt)