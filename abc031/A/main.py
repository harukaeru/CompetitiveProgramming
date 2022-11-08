#!/usr/bin/env python3.8
A, D = map(int, input().split())

m = min(A, D) + 1
print(max(A, D) * m)