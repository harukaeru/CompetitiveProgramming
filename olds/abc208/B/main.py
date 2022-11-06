#!/usr/bin/env python3.8
P = int(input())

def factorial(k):
    s = 1
    while k > 0:
        s *= k
        k -= 1
    return s

*coins, = reversed(list(map(factorial, range(1, 11))))

s = 0
for c in coins:
    n = int(P // c)
    if n == 0:
        continue

    P = P - (n * c)
    s += n
    if P == 0:
        print(s)
