#!/usr/bin/env python3.8
X = int(input())
def s(n):
  return n * (n + 1) // 2

for i in range(0, 60000):
  if X <= s(i):
    print(i)
    exit()