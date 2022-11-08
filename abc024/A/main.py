#!/usr/bin/env python3.8
A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

p = S * A + T * B
if S + T >= K:
  p -= (S + T) * C
print(p)