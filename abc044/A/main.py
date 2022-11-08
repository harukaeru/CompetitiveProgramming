#!/usr/bin/env python3.8
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(min(N, K) * X + max(0, N - K) * Y)