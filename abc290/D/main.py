#!/usr/bin/env python3.8
from math import gcd


T = int(input())
for i in range(T):
  N,D,K=map(int, input().split())
  K -= 1

  L = gcd(N, D)
  L = (N * D) // L
  print('L', L)
  alpha = L // D
  print(D * (K + alpha) + K // alpha)