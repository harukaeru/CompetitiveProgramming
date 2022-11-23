#!/usr/bin/env python3.8
import bisect
S = input()
K = int(input())

T = [0] * (1 + len(S))
for i in range(len(S)):
  T[i + 1] = T[i] + (1 if S[i] == '.' else 0)

Q = []
for t in T:
  Q.append(max(t - K, 0))

mc = 0
for i, q in enumerate(Q):
  j = bisect.bisect_left(T, q)
  cnt = i - j
  mc = max(mc, cnt)
  # print((j,i), cnt)
print(mc)