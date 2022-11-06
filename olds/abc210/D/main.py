#!/usr/bin/env python3.8
H, W, C = map(int, input().split())

HW = []
for i in range(H):
    *w, = map(int, input().split())
    HW.append(w)

dp = None
dpx = None

def init():
    global dp
    global dpx
    dp = [
        [float('inf') for __ in range(W)]
        for ___ in range(H)
    ]

    dpx = [
        [float('inf') for __ in range(W)]
        for ___ in range(H)
    ]

def reverse(HW):
    revs = []
    for h in HW:
        revs.append(list(reversed(h)))
    return revs

def set_dp(A):
    for i in range(H):
        for j in range(W):
            comps = [A[i][j]]

            if i != 0:
                comps.append(dp[i - 1][j] + C)
            if j != 0:
                comps.append(dp[i][j - 1] + C)
            dp[i][j] = min(comps)

def set_dpx(A):
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            comps = []

            if i != 0:
                comps.append(dp[i - 1][j] + C)
            if j != 0:
                comps.append(dp[i][j - 1] + C)
            dpx[i][j] = A[i][j] + min(comps)

def get_min(A):
    min_v = float('inf')

    for i in range(H):
        for j in range(W):
            min_v = min(min_v, dpx[i][j])
    return min_v

init()
set_dp(HW)
set_dpx(HW)
m = get_min(HW)

# for d in dp:
#     print(d)
# print('dpx-'*20)
# for d in dpx:
#     print(d)
init()
reversed_HW = reverse(HW)
set_dp(reversed_HW)
set_dpx(reversed_HW)
# print('-'*20)
# for d in dpx:
#     print(d)
print(min(m, get_min(reversed_HW)))
