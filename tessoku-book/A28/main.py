#!/usr/bin/env python3.8
N = int(input())
mod = 10000
v = 0
for i in range(N):
  t,a = input().split()
  a = int(a)
  if t == '+':
    v += a
  elif t == '-':
    v -= a
  elif t == '*':
    v *= a
  v %= mod
  print(v)

