#!/usr/bin/env python3.8
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
  dp[i] = dp[i - 1] + max(0, a[i - 1])

print(dp)
print(dp[n])