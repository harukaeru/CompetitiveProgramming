#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
  print(1)
  exit()

one_pos = A.index(1)
A = A[:one_pos] + A[one_pos + 1:]

cnt = 0
for i in range(0, N - 1, K - 1):
  # print(A[i:i+K-1])
  cnt += 1

print(cnt)
