#!/usr/bin/env python3
import math
A, B, C, D = map(int, input().split())

l = C * D // math.gcd(C, D)

c_count = B // C - (A - 1) // C
d_count = B // D - (A - 1) // D
cd_count = B // l - (A - 1) // l

# print('c_count', c_count)
# print('d_count', d_count)
# print('cd_count', cd_count)
ng = c_count + d_count - cd_count

print((B - A + 1) - ng)