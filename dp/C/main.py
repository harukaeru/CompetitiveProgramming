#!/usr/bin/env pypy3
N = int(input())
A = []
B = []
C = []
for i in range(N):
  a,b,c = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)

dp = []
for i in range(1 + N):
  d = [0] * 3
  dp.append(d)

for i in range(1, 1 + N):
  a = A[i - 1]
  b = B[i - 1]
  c = C[i - 1]

  dp[i][0] = max(a + dp[i - 1][1], a + dp[i - 1][2])
  dp[i][1] = max(b + dp[i - 1][0], b + dp[i - 1][2])
  dp[i][2] = max(c + dp[i - 1][0], c + dp[i - 1][1])

print(max(dp[N]))