#!/usr/bin/env python3
N = int(input())

sq = int(N ** (1 / 2))

expressable_set = set()

for a in range(2, sq + 1):
    x = a * a
    while x <= N:
        expressable_set.add(x)
        x *= a

print(N - len(expressable_set))
