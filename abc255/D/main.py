#!/usr/bin/env python3.8
import bisect
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
s = sum(A)

S1 = [0] * (N + 1)
for i in range(1, N + 1):
  S1[i] = S1[i - 1] + A[i - 1]

S2 = [0] * (N + 1)
for i in range(N, 0, -1):
  S2[i - 1] = S2[i] + A[i - 1]

def query(q):
  idx = bisect.bisect_left(A, q)
  s1 = 0 if idx == 0 else idx * q - S1[idx]

  idx = bisect.bisect_right(A, q)
  s2 = 0 if idx == N else S2[idx] - (N - idx) * q
  return s1 + s2

for i in range(Q):
  q = int(input())
  print(query(q))