#!/usr/bin/env python3.8
N = int(input())
m = 9999999999999999
for i in range(N):
  m = min(m, int(input()))
print(m)