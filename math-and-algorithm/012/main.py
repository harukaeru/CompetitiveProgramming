#!/usr/bin/env python3.8
import math
N = int(input())

for i in range(2, int(math.sqrt(N)) + 1):
  if N % i == 0:
    print('No')
    exit()

print('Yes')