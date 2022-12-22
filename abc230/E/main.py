#!/usr/bin/env python3.8
N = int(input())

L = 1
ans = 0
while L <= N:
  k = N // L
  R = N // k
  ans += (R - L + 1) * k
  L = R + 1
print(ans)