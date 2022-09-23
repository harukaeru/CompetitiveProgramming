#!/usr/bin/env python3
import math
N = int(input())

primes = []

for n in range(2, N + 1):
  is_prime = True
  for p in primes:
    if n % p == 0:
      is_prime = False
      break
  if is_prime:
    primes.append(n)

print(' '.join(map(str, primes)))