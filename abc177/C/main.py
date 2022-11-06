#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7
tot = 0
S = [0] * N
for i in range(N - 1, -1, -1):
  if i == N - 1:
    S[i] = A[i]
  else:
    S[i] = A[i] + S[i + 1]
  S[i] %= MOD

for i in range(N - 1):
  a = A[i]
  s = S[i + 1]
  tot += a * s % MOD

print(tot % MOD)