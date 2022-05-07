#!/usr/bin/env python3
N = int(input())

t = 0
if N >= 1000:
    t += N - 1000 + 1

if N >= 10 ** 6:
    t += N - 10 ** 6 + 1

if N >= 10 ** 9:
    t += N - 10 ** 9 + 1

if N >= 10 ** 12:
    t += N - 10 ** 12 + 1

if N >= 10 ** 15:
    t += N - 10 ** 15 + 1

print(t)

