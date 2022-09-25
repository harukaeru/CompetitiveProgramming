#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

e = 0
for i in range(N):
  e += A[i] / 3 + B[i] * 2 / 3

print(e)