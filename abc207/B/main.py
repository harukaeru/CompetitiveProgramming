#!/usr/bin/env python3
a, b, c, d = map(int, input().split())

for i in range(100001):
    s = a + b * i
    r = c * i
    if r * d >= s:
        print(i)
        exit()
print(-1)
