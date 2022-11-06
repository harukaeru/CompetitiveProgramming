#!/usr/bin/env python3.8
import math
N = int(input())


maximum = -1
for i in range(int(math.log(10 ** 18, 2) + 1)):
    if 2 ** i <= N:
        maximum = i
    else:
        break

print(maximum)
