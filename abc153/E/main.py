#!/usr/bin/env pypy3
H, N = map(int, input().split())
A = []
B = []
for i in range(N):
  a,b = map(int, input().split())
  A.append(a)
  B.append(b)

inf = 1e18
dp = []
for i in range(N + 1):
  d = [inf] * (1 + H)
  dp.append(d)
dp[0][H] = 0

for i in range(1, N + 1):
  a = A[i - 1]
  b = B[i - 1]
  for j in range(H, -1, -1):
    dp[i][j] = min(dp[i][j], dp[i - 1][j])
    dam = max(0, j - a)
    # print(dam, end=' ')
    dp[i][dam] = min(dp[i][dam], dp[i][j] + b)
  # print(dp[i])
# for d in dp:
#   print(d)
print(dp[N][0])