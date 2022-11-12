#!/usr/bin/env python3.8
import math
N = int(input())
x = int(math.sqrt(N))

ans = 99999999999
for i in range(1, x + 1):
  j = N // i
  diff = j - i
  rest = N - i * j
  pans = diff + rest
  ans = min(ans, pans)

print(ans)
