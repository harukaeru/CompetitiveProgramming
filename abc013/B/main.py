#!/usr/bin/env python3.8
a = int(input())
b = int(input())

k = abs(a - b)
print(min(k, 10 - k))