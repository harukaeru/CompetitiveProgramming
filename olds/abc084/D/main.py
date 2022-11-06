#!/usr/bin/env python3.8
import math

Q = int(input())

maxlr = -1

queries = []
for __ in range(Q):
    l, r = map(int, input().split())
    queries.append([l, r])
    maxlr = max(max(maxlr, l), r)

primes = []
for i in range(2, maxlr + 1):
    p = int(math.sqrt(i))
    is_prime = True
    for pp in range(2, p + 1):
        if i % pp == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)

primeset = set(primes)
neo_primes = []
for p in primes:
    if (p + 1) % 2 == 0:
        np = ((p + 1) // 2)
        if np in primeset:
            neo_primes.append(p)

P = [0] * (maxlr + 1)
for p in neo_primes:
    P[p] += 1

S = [0] * (maxlr + 2)
for i in range(len(P)):
    S[i+1] = S[i] + P[i]

for q in queries:
    l, r = q
    print(S[r + 1] - S[l])
