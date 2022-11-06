#!/usr/bin/env python3.8
S = []

A = 999999
B = 0
C = 999999
D = 0
for i in range(10):
  s = input()
  for j in range(10):
    if s[j] == '#':
      A = min(A, i + 1)
      B = max(B, i + 1)
      C = min(C, j + 1)
      D = max(D, j + 1)
      
print(A, B)
print(C, D)