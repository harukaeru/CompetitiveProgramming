#!/usr/bin/env python3.8
N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
  A.append(0)

print(*A[K:])