#!/usr/bin/env python3.8
import math
N, X = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for x_i in x:
  ans = math.gcd(ans, abs(X - x_i))

print(ans)