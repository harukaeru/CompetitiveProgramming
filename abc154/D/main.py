#!/usr/bin/env python3.8
N, K = map(int, input().split())
P = list(map(int, input().split()))

es = []
for i in range(N):
  p = P[i]
  e = (p * (p + 1) / 2) / p
  es.append(e)
# print(es)

me = sum(es[:K])
cur = me
for i in range(K, N):
  cur = cur + es[i] - es[i - K]
  me = max(me, cur)
print(me)