#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

max_a = 0
i_maxs = [None] * N
for i in range(N):
  max_a = max(max_a, A[i])
  i_maxs[i] = max_a

max_a = 0
j_maxs = [None] * N
for j in range(N - 1, -1, -1):
  max_a = max(max_a, A[j])
  j_maxs[j] = max_a

for k in range(N):
  ii = 0
  if k - 1 >= 0:
    ii = i_maxs[k - 1]

  jj = 0
  if k + 1 < N:
    jj = j_maxs[k + 1]
  
  print(max(ii, jj))