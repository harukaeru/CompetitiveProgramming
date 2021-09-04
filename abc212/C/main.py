#!/usr/bin/env python3
N, M = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())

A = sorted(A)
B = sorted(B)

i = 0
j = 0
d = 999999999999
while (i < N and j < M):
    m = abs(A[i] - B[j])
    d = min(d, m)
    if (A[i] < B[j]):
        i += 1
    else:
        j += 1
print(d)
