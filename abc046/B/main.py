#!/usr/bin/env python3.8
N, K = map(int, input().split())

print(K * ((K - 1) ** (N - 1)))