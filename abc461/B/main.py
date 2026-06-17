#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for ax_i in range(N):
  kikori_i = B[ax_i] - 1
  if ax_i + 1 == A[kikori_i]:
    continue
  print('No')
  exit()
print('Yes')