#!/usr/bin/env python3.8
N,M=map(int, input().split())
A = list(map(int, input().split()))

count = [0] * (N + 2)
for i in range(M):
  count[A[i]] += 1

found = [0] * (N + 2)
for i, c in enumerate(count):
  if c == 0:
    found[i] = 1
    break

for i in range(M, N):
  count[A[i - M]] -= 1
  count[A[i]] += 1

  found[A[i - M]] |= count[A[i - M]] == 0

# print(found)
for i in range(N + 2):
  if found[i] != 0:
    print(i)
    break