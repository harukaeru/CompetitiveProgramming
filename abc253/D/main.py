#!/usr/bin/env python3
import math
N, A, B = map(int, input().split())

g = math.gcd(A, B)
m = A * B // g
def get_tot(k):
  if k > N:
    return 0
  n = N // k
  cnt = n * (k + n * k) // 2
  return cnt

# |A| ∨ |B| = |A| + |B| - |A| ∧ |B|

# print('A', get_tot(A))
# print('B', get_tot(B))
# print('m', get_tot(m))
aorb = get_tot(A) + get_tot(B) - get_tot(m)

print(N * (N + 1) // 2 - aorb)