#!/usr/bin/env pypy3


N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for j in range(K + 1):
  dp.append([None] * D)
dp[0][0] = 0

for i in range(1, N + 1):
  a = A[i - 1]
  for j in range(K - 1, -1, -1):
    d = dp[j]

    for p, xx in enumerate(d):
      if xx is None:
        continue
      dv = D * xx + p
      if j + 1 <= K:
        yy = (dv + a) % D
        dp[j + 1][yy] = max(dp[j+1][yy] if dp[j +1][yy] else 0, (dv + a) // D)

# print(dp)
v = dp[K][0]
if v is None:
  print(-1)
else:
  print(v * D)