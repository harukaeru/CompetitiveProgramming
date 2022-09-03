#!/usr/bin/env python3
L, R = map(int, input().split())


m = 99999999999
for i in range(L, R):
  for j in range(L + 1, R + 1):
    v = (i % 2019) * (j % 2019) % 2019
    m = min(m, v)

print(m)
