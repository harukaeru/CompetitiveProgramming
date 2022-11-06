#!/usr/bin/env python3.8
import math
N = int(input())
A = list(map(int, input().split()))

L = [0] * (N + 1)
R = [0] * (N + 1)
for i in range(N):
  L[i+1] = math.gcd(A[i], L[i])
for j in range(N - 1, -1, -1):
  R[j] = math.gcd(A[j], R[j + 1])

max_g = -1
for i in range(N):
  g_0 = L[i]
  g_1 = R[i + 1]
  # left = A[:i]
  # right = A[i+1:]

  # g_0 = 0
  # for l in left:
  #   g_0 = math.gcd(g_0, l)

  # g_1 = 0
  # for r in right:
  #   g_1 = math.gcd(g_1, r)
  g = math.gcd(g_0, g_1)
  max_g = max(max_g, g)
print(max_g)