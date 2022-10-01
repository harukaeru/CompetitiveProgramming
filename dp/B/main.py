#!/usr/bin/env python3
N, K = map(int, input().split())
h = list(map(int, input().split()))

# sh = [0] * (N + 1)
# for i, v in enumerate(h):
#   sh[i + 1] = sh[i] + v
# print(sh)

dp = [9999999999999] * (N + 1)
dp[1] = 0
# pos= [1, N]
for pos in range(1, N + 1):
  # k = [1, k - 1]
  for k in range(1, K + 1):
    if pos + k - 1 < N:
      dp[pos + k] = min(dp[pos + k], dp[pos] + abs(h[pos - 1] - h[pos + k - 1]))

# print(dp)
print(dp[N])