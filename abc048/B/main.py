#!/usr/bin/env python3.8
a, b, x = map(int, input().split())

ca = (a + x - 1) // x
cb = b // x
print(cb - ca + 1)