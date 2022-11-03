#!/usr/bin/env pypy3
import math
a, N = map(int, input().split())

rest = 1000

dp = []
for i in range(rest + 1):
  dp.append(set())

M = 10 ** (len(str(N)) + 1)

dp[0] = [1]

checked = set()

for i in range(1, rest + 1):
  for d in dp[i - 1]:
    k = d * a
    if k < M and k not in checked:
      dp[i].add(k)
    if d >= 10 and d % 10 != 0:
      n = int(str(d % 10) + str(d // 10))
      if n < M and n not in checked:
        dp[i].add(n)
  # print('dp', dp[i])
  if N in dp[i]:
    print(i)
    exit()
  checked.update(dp[i])

print(-1)
