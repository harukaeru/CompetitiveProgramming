#!/usr/bin/env python3.8
N = int(input())
A = [1e18, 1e18] + list(map(int, input().split()))
B = [1e18, 1e18, 1e18] + list(map(int, input().split()))

dp = [1e18] * (1 + N)
dp[1] = 0

for i in range(2, 1 + N):
  dp[i] = min(dp[i], dp[i - 1] + A[i])
  dp[i] = min(dp[i], dp[i - 2] + B[i])

routes = [N]
d = dp[N]
i = N
while i > 1:
  if dp[i] == dp[i - 1] + A[i]:
    routes.append(i - 1)
    i -= 1
  else:
    routes.append(i - 2)
    i -= 2
  
routes.reverse()
print(len(routes))
print(*routes)