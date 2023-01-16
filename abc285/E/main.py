#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

m = 0
cache = {}
def calc_production(d):
  if cache.get(d):
    return cache[d]

  tot = 0
  for i in range(d):
    tot += A[i // 2]
  cache[d] = tot
  return tot

dp = []
for i in range(1 + N):
  dp.append([-1e5] * (1 + N))

dp[1][0] = 0

for i in range(N):
  for j in range(N):
    if dp[i][j] < 0:
      continue
    # 休みでないときは値をそのままにして次へ（今は足さないが、将来休みがきたときに最後に足す） -> ①へ
    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
    # 休みのときはcalculation発動。平日が続いた分(休日の間隔から得られる値を足す)
    dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + calc_production(j))

m = -1e18
for j, d in enumerate(dp[N]):
  if d < 0:
    continue
  # ①: ここで最後の足し算処理をしている
  m = max(m, d + calc_production(j))
print(m)