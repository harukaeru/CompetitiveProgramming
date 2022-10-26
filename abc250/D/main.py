#!/usr/bin/env python3
import bisect
N = int(input())

qs = int(N ** (1/3) + 1)

primes = [True] * qs
primes[0] = False

for i in range(2, qs + 1):
  for j in range(i * 2, qs + 1, i):
    primes[j - 1] = False

ps = []
for i, p in enumerate(primes, 1):
  if p:
    ps.append(i)
# print(ps)

cnt = 0
for q in ps:
  t = q ** 3
  p = N // t

  m = min(p + 1, q)
  # print('p,q', p, q, m)
  cnt += bisect.bisect_left(ps, m)
print(cnt)