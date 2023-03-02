#!/usr/bin/env python3.8
Q = int(input())

P = [0] * 300000
P[0] = 1

for i in range(2, 150000):
  for j in range(2 * i, 300001, i):
    P[j - 1] = 1

primes = []
for i, v in enumerate(P):
  if v == 0:
    primes.append(i + 1)
# print(primes)
primes = set(primes)

for i in range(Q):
  x = int(input())
  if x in primes:
    print('Yes')
  else:
    print('No')