#!/usr/bin/env python3.8
N, K, R = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * (N + 1)
for i in range(1, N + 1):
  D[i] = D[i - 1] + A[i - 1]

E = [0] * (N + 1)
for i in range(N, 0, -1):
  E[i - 1] = E[i] + A[i - 1]

for i in range(1, N + 1):
  D[i] -= i * K

for i in range(N, 0, -1):
  E[i - 1] -= (N - i + 1) * R

for i in range(1, N + 1):
  D[i] = max(D[i - 1], D[i])

for i in range(N, 0, -1):
  E[i - 1] = max(E[i], E[i - 1])

m = 0
for i in range(0, N + 1):
  m = max(m, D[i] + E[i])

print(sum(A) - m)