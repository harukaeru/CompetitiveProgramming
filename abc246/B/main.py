#!/usr/bin/env python3.8
import math
A, B = map(int, input().split())


rate = 1 / math.sqrt(A * A + B * B)

print(rate * A, rate * B)