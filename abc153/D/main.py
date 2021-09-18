#!/usr/bin/env python3
H = int(input())

cache = {}

def calc_m(m):
    if m == 1:
        return 1
    if cache.get(m):
        return cache[m]
    h = m // 2
    cache[m] = 1 + calc_m(h) + calc_m(h)
    return cache[m]

print(calc_m(H))
