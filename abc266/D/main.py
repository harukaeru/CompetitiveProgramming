#!/usr/bin/env python3
N = int(input())
T = []
X = []
A = []
for i in range(N):
  t,x,a = map(int, input().split())
  T.append(t)
  X.append(x)
  A.append(a)

dp = [None] * 5
dp[0] = 0

current_time = 0
for i in range(1, N + 1):
  t = T[i - 1]
  size = A[i - 1]
  pos = X[i - 1]
  diff = t - current_time
  start = max(0, pos - diff)
  end = min(pos + diff + 1, 5)

  ndp = []
  for k, d in enumerate(dp):
    ddp = [d for d in dp[max(k - diff, 0):min(k+diff+1, 5)] if d is not None]
    ndp.append(max(ddp) if ddp else None)
  
  prevs = [dp[j] for j in range(start, end) if dp[j] is not None]
  if prevs:
    m = max(prevs) + size
    ndp[pos] = m

  dp = ndp
  current_time = t
  # print(dp)

print(max([d for d in dp if d is not None]))