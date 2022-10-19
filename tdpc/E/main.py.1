#!/usr/bin/env python3
D = int(input())
N = int(input())
S = str(N)

MOD = 1000000007

dp = []
for i in range(len(S) + 1):
  d = []
  for smaller in [False, True]:
    xd = [0] * D
    d.append(xd)
  dp.append(d)

def get_digit(digit):
  c = ord(S[digit]) - ord('0')
  return c

dp[0][0][0] = 1
for i in range(len(S)):
  for j in range(D):
    for k in range(10):
      dp[i + 1][True][(j + k) % D] += dp[i][True][j]
      dp[i + 1][True][(j + k) % D] %= MOD
    
    num = get_digit(i)
    for k in range(num):
      dp[i + 1][True][(j + k) % D] += dp[i][0][j]
      dp[i + 1][True][(j + k) % D] %= MOD
    
    dp[i + 1][False][(j + num) % D] = dp[i][0][j]

for d in dp:
  print('------')
  print(d)
print(dp[len(S)][False][0] + dp[len(S)][True][0] - 1)