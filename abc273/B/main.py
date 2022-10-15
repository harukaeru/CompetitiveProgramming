#!/usr/bin/env python3
X, K = map(int, input().split())

for i in range(K):
  p = X // (10 ** i)
  q = p % 10
  t = p // 10

  if q >= 5:
    X = (t + 1) * (10 ** (i + 1))
  else:
    X = t * (10 ** (i + 1))

print(X)