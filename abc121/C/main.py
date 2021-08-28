#!/usr/bin/env python3

N, M = map(int, input().split())

L = []
for i in range(N):
    A_i, B_i = map(int, input().split())
    L.append([A_i, B_i])

L.sort(key=lambda x: x[0])

m = 0
l_idx = 0
for i in range(M):
    if L[l_idx][1] == 0:
        l_idx += 1
    L[l_idx][1] = L[l_idx][1] - 1
    m += L[l_idx][0]

print(m)
