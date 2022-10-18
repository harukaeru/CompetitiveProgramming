#!/usr/bin/env python3
N = int(input())

S = str(N)

dp = []
for i in range(len(S) + 1):
  d = [
    # 1を選んだ個数
    [0] * (len(S) + 1),
    [0] * (len(S) + 1),
  ]
  dp.append(d)

# 1桁も選んでいなくて、1を1回も使っていない
dp[0][False][0] = 1
for i in range(len(S)):
  # Nより小さい数のとき。1を選んだら1つ増やし、1を選んでないときは前の数をそのまま使う
  for j in range(len(S)):
    dp[i + 1][True][j + 1] += dp[i][True][j]
    dp[i + 1][True][j] += dp[i][True][j] * 9

  # ある桁の数。0からこの数値までしか探索できない
  num = ord(S[i]) - ord('0')

  # Nと同じ場所
  for j in range(len(S)):
    if num == 1:
      dp[i + 1][True][j] += dp[i][False][j]
    elif num > 1:
      dp[i + 1][True][j] += dp[i][False][j] * (num - 1)
      dp[i + 1][True][j + 1] += dp[i][False][j]

    if num == 1:
      dp[i + 1][False][j + 1] += dp[i][False][j]
    else:
      dp[i + 1][False][j] += dp[i][False][j]
  # print(dp[i + 1])


# for i, d in enumerate(dp):
#   print(S[:i] + '*' * len(S[i:]) + ':')
#   print('       1の個数')
#   print('  未満', d[True])
#   print('  同一', d[False])

tot = 0
for i in range(len(S) + 1):
  tot += dp[len(S)][True][i] * i
  tot += dp[len(S)][False][i] * i
print(tot)
# print(dp[len(S)][True][True] + dp[len(S)][False][True])