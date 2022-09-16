#!/usr/bin/env python3
import bisect
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S_a = [0] * (N + 1)
for i in range(N):
  S_a[i + 1] = A[i] + S_a[i]

S_b = [0] * (M + 1)
for i in range(M):
  S_b[i + 1] = B[i] + S_b[i]

max_books = 0
for i in range(N + 1):
  candidate_s_b = K - S_a[i]
  if candidate_s_b < 0:
    continue

  j = bisect.bisect_right(S_b, candidate_s_b) - 1
  max_books = max(max_books, i + j)

print(max_books)