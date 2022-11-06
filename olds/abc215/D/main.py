#!/usr/bin/env python3.8
import math

N, M = map(int, input().split())

*A, = map(int, input().split())

# print(N, M)
# print(A)
maxA = max(A)

# 1, 2, 3, 4, 5, ... M
is_prime_list = [True] * maxA
ok_list = [True] * max(maxA, M)
# print(is_prime_list)

for a in A:
    ok_list[a - 1] = False

# print('a_bit', ok_list)

primes = []
for i in range(2, maxA + 1):
    if not is_prime_list[i - 1]:
        continue

    # print('i', i)
    for j in range(i * 2, maxA+1, i):
        is_prime_list[j - 1] = False
        ok_list[i - 1] = ok_list[i - 1] and ok_list[j - 1]

    if not ok_list[i - 1]:
        primes.append(i)

# print('primes', primes)
a_list = [True] * M

for p in primes:
    for i in range(p, M +1, p):
        a_list[i - 1] = False

ans = []
for i, b in enumerate(a_list):
    if b:
        ans.append(i + 1)

print(len(ans))
for a in ans:
    print(a)
