#!/usr/bin/env python3
N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)

for i in range(N):
  S[i + 1] = S[i] + A[i]

x = 0
for i in range(M):
  x += (i + 1) * A[i]

S2 = [0] * (N - M + 1)
S2[0] = x
for i in range(1, N - M + 1):
  partial = S[i + M - 1] - S[i - 1]
  S2[i] = S2[i - 1] - partial + M * A[i + M - 1]
print(max(S2))