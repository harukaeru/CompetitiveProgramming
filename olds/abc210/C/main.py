#!/usr/bin/env python3.8
from collections import deque
N, K = map(int, input().split())
*C, = map(int, input().split())

dp = {}
total = 0

def add_one(dp, v):
    global total
    if not dp.get(v):
        dp[v] = 0
    if dp[v] == 0:
        total += 1
    dp[v] += 1

def remove_one(dp, v):
   global total
   dp[v] -= 1
   if dp[v] == 0:
        total -= 1

for i in range(K):
    add_one(dp, C[i])

m = total
for i in range(1, N - K + 1):
    # print('dp', dp, total)
    # print('dp', i + K - 1)
    # print('dp', C[i + K - 1])
    remove_one(dp, C[i - 1])
    add_one(dp, C[i + K - 1])
    m = max(m, total)

print(m)
