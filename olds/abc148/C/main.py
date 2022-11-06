#!/usr/bin/env python3.8

A, B = map(int, input().split())

def gcd(a, b):
    if b == 1:
        return 1

    r = a % b
    if r == 0:
        return b

    return gcd(b, r)

k = gcd(A, B)
print(int(A * B / k))
