#!/usr/bin/env python3.8
N = int(input())

L = int((N ** (1/3) + 1) ** 3)

def f(a, b):
  p = a ** 2
  q = b ** 2
  return p * a + p * b + a * q + b * q

X = 9999999999999999999
j = 1000000
for i in range(0, 1000001):
  while f(i, j) >= N and j >= 0:
    print(f'f({i},{j})', f(i,j))
    X = min(X, f(i, j))
    j -= 1

print(X)