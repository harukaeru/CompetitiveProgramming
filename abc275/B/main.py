#!/usr/bin/env python3
MOD = 998244353 
A, B, C, D, E, F = map(int, input().split())

print(((A * B * C) - (D * E * F)) % MOD)