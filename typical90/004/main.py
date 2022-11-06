#!/usr/bin/env python3.8
H, W = map(int, input().split())
HW = []
for i in range(H):
    w = list(map(int, input().split()))
    HW.append(w)

h_sums = []
for i in range(H):
    h_sums.append(sum(HW[i]))

w_sums = []
for j in range(W):
    s = 0
    for i in range(H):
        s += HW[i][j]
    w_sums.append(s)

for i in range(H):
    res = []
    for j in range(W):
        res.append(h_sums[i] + w_sums[j] - HW[i][j])
    print(*res)