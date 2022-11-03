#!/usr/bin/env python3
A, B, N = map(int, input().split())


K = min(B - 1, N)
print((A * K // B) - A * (K // B))