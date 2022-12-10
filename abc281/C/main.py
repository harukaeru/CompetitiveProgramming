#!/usr/bin/env python3.8
import bisect


N, T = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (1 + N)
for i in range(N):
  a = A[i]
  B[i + 1] = A[i] + B[i]

# print(B)
s = sum(A)
t = T % s
# print('t', t)
pos = bisect.bisect_left(B, t)
pos = pos if B[pos] == t else pos - 1
print(pos + 1, t - B[pos])