#!/usr/bin/env python3

A, B = map(int, input().split())

for c in range(256):
    if A ^ B == c:
        print(c)
        break
