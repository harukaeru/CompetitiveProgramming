#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

s = sum(A)
t = 0
for a in A:
  t += a * a

def calc(x):
  return t - 2 * x * s + N * x * x

m = 1e18
for i in range(-100, 101):
  c = calc(i)
  # print(i, c)
  if m > c:
    m = c

print(m)