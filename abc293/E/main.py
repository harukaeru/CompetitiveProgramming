#!/usr/bin/env python3.8
from math import gcd


A,X,M=map(int, input().split())

# def mod_pow(x: int, n: int):
#     bi = str(format(n, "b"))
#     res = 1
#     a = x
#     print('bi', bi)
#     for i in range(len(bi)):
#         if n >> i & 1:
#             res = (res * a) % M
#         a = (a * a) % M
#     return res
if A == 1:
  print(X % M)
  exit()

u = (pow(A, X, M * (A - 1)) - 1)
d = (A- 1)

print((u // d) % M)