#!/usr/bin/env python3.8
N,S=map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(1 + N):
  d = [False] * (1 + S)
  dp.append(d)

dp[0][0]=True

for i in range(1, 1 + N):
  a = A[i - 1]
  for j in range(S + 1):
    dp[i][j] = dp[i][j] or dp[i - 1][j]
    if j + a <= S:
      dp[i][j + a] = dp[i][j + a] or dp[i - 1][j]

if not dp[N][S]:
  print(-1)
  exit()

s = S
choices = []
i = N
for i in range(N, 0, -1):
  if s - A[i - 1] >= 0 and dp[i][s - A[i - 1]]:
    choices.append(i)
    s -= A[i - 1]

choices.sort()
print(len(choices))
print(*choices)
# print(*[A[c] for c in choices])
# print(sum([A[c] for c in choices]))
# print(*[A[c] for c in choices])
# print(dp[N][S])