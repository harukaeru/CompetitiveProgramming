#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

s = 0
for i in range(N):
  a = A[i]
  s += a ** 2

s *= (N - 1)
tot = sum(A)
x = 0
for i in range(N):
  a = A[i]
  x += a * (tot - a)

s -= x
print(s)