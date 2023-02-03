#!/usr/bin/env python3.8
N = int(input())
P = [1e18] * (N + 10)
A = [1e18] * (N + 10)
for i in range(N):
  p,a=map(int, input().split())
  P[i + 1] = p
  A[i + 1] = a

# print(P)
dp = []
l = 1
r = N
for i in range(N + 2):
  d = [0] * (2 + N)
  dp.append(d)

for le in range(N - 2, -1, -1):
  for l in range(1, N - le + 1):
    r = l + le

    score1 = A[l - 1] if l <= P[l - 1] <= r else 0
    score2 = A[r + 1] if l <= P[r + 1] <= r else 0

    dp[l][r] = max(
      dp[l][r],
      dp[l - 1][r] + score1,
      dp[l][r + 1] + score2
    )

 #    print(
 #      '-----in:',
 #      dp[l - 1][r] + score1,
 #      dp[l][r + 1] + score2
 #    )
 #    print(f'P[{l-1}]', P[l-1])
 #    print(f'P[{r}]', P[r])
 #    print((l, r), '<-', (l-1, r), (l, r + 1), '=', dp[l][r])
 #  print('------------------------le:', le)

ans = 0
for i in range(1, N + 1):
  ans = max(ans, dp[i][i])

print(ans)