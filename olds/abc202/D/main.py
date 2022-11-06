#!/usr/bin/env python3.8
import math

A, B, K = map(int, input().split())


def pop(A, B):
    global K
    c = math.comb(A + B - 1, B)

    if c < K:
        B = B - 1
        K = K - c
        print('b', end='')
    else:
        A = A - 1
        print('a', end='')
    if A + B == 0:
        return

    pop(A, B)

pop(A, B)
print()
