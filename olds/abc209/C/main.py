#!/usr/bin/env python3.8

MOD = 1000000007

N = int(input())
*C, = map(int, input().split())
C = sorted(C)

ans = 1
for i, c in enumerate(C):
    ans = max(0, ans * (c - i) % MOD)
print(ans)
