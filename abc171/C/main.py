#!/usr/bin/env python3
N = int(input())

d = -1
for i in range(1, 12):
  k = 26 ** i
  if N <= k:
    d = i
    break
  N -= k

ans = ''
N -= 1
for i in range(d):
  k = N % 26
  ans = chr(ord('a') + k) + ans
  N //= 26

print(ans)