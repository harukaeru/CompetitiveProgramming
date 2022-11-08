#!/usr/bin/env python3.8
N = int(input())
b = bin(N).replace('0b', '')
ans = []
for i, p in enumerate(b):
  a = (2 ** i) * (p == '1')
  if a:
    ans.append(a)

print(len(ans))
for a in ans:
  print(a)