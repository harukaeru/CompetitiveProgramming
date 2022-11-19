#!/usr/bin/env python3.8
A = []
for i in range(4):
  A.append(input().split())

for i in range(4):
  print(*reversed(A[4 - i - 1]))