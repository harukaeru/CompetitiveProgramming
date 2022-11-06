#!/usr/bin/env python3.8
N = int(input())
x = 0
for i in range(N):
  p, q = map(int, input().split())
  x += q / p

print(x)