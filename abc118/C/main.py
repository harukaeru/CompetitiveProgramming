#!/usr/bin/env python3.8
import math
N = int(input())
A = list(map(int, input().split()))

g = 9999999999
for i in range(N - 1):
  g = math.gcd(A[i], A[i + 1])
  A[i + 1] = g


print(g)