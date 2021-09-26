#!/usr/bin/env python3
A, B, C = map(int, input().split())

for i in range(1000000):
    x = C * (i + 1)
    if A <= x <= B:
        print(x)
        exit()
print(-1)
