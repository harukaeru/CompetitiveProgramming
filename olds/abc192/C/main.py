#!/usr/bin/env python3.8
N, K = map(int, input().split())


def f(x):
    x2 = sorted(map(int, list(str(x))))
    g2 = int(''.join(map(str, [y for y in x2])))
    x2.reverse()
    g1 = int(''.join(map(str, [y for y in x2])))
    return g1 - g2

x = N
while K > 0:
    x = f(x)
    K -= 1
print(x)
