#!/usr/bin/env python3.8
from collections import Counter
MOD = 10 ** 9 + 7


N,M=map(int, input().split())
S = []
for i in range(N):
  S.append(int(input()))

l = 0
r = 0
cur = Counter()
ran = [0] * (1 + N)
while r < N:
  cur[S[r]] += 1

  while l < r and cur[S[r]] > 1:
    cur[S[l]] -= 1
    l += 1

  ran[r + 1] = l
  r += 1


# for r in range(1, N + 1):
#   print(ran[r], r, S[max(ran[r], 0):r])
# print(ran)

dp = [0] * (1 + N)
sum = [0] * (2 + N)
dp[0] = 1
sum[1] = 1
for i in range(1, 1 + N):
  l, r = ran[i], i
  dp[r] = (sum[r] - sum[l]) % MOD
  sum[r + 1] = (sum[r] + dp[r]) % MOD
  # for j in range(l, r):
  #   dp[i] += dp[j]

print(dp[N])