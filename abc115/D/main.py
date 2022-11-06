#!/usr/bin/env python3.8
N, X = map(int, input().split())

P = [0] * (N + 1)
L = [0] * (N + 1)
def set_len(n):
  if n == 0:
    P[0] = L[0] = 1
    return (1, 1)

  b = set_len(n - 1)

  p = 1 + b[0] * 2
  l = 3 + b[1] * 2
  P[n] = p
  L[n] = l
  return (p, l)

set_len(N)

def solve(n, x):
  if n == 0:
    return 1

  if x == 1:
    return 0
  elif x <= 1 + L[n - 1]:
    return solve(n - 1, x - 1)
  elif x == 2 + L[n - 1]:
    return P[n - 1] + 1
  elif x <= 2 + 2 * L[n - 1]:
    return P[n - 1] + 1 + solve(n - 1, x - L[n - 1] - 2)
  else:
    return 2 * P[n - 1] + 1
  # 'B' + L[n - 1] + 'P' + L[n - 1] + 'B'

print(solve(N, X))
  