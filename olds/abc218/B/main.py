#!/usr/bin/env python3.8
*P, = map(int, input().split())

num = ord('a')
for p in P:
    print(chr(num + p - 1), end='')
print()
