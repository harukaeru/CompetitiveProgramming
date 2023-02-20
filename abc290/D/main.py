#!/usr/bin/env python3.8
from math import gcd


T = int(input())
for i in range(T):
  N,D,K=map(int, input().split())
  K -= 1

  f = N // gcd(N, D)
  print('f', f)
  print((D * (K % f)) % N + K // f)