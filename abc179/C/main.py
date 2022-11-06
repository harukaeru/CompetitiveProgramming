#!/usr/bin/env python3.8
import math
N = int(input())

cnt = 0
for a in range(1, N):
  cnt += (N - 1) // a
print(cnt)  
