#!/usr/bin/env python3.8
A, B, C, D = map(int, input().split())

primes = [True] * 201
primes[0] = False
primes[1] = False
for i in range(2, 201):
  for j in range(2 * i, 201, i):
    primes[j] = False
  
ps = []
for p, v in enumerate(primes):
  if v:
    ps.append(p)

# print(ps)

found_primes = []
for i in range(A, B + 1):
  found = False
  for j in range(C, D + 1):
    if i + j in ps:
      found = True
  found_primes.append(found)

if all(found_primes):
  print('Aoki')
else:
  print('Takahashi')