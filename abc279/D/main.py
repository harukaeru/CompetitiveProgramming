#!/usr/bin/env python3.8
from decimal import Decimal


A, B = map(int, input().split())

x = (Decimal(A) / (Decimal(2) * Decimal(B))) ** (Decimal(2)/Decimal(3))
x = int(x)

mr = 99999999999999999999999
for i in range(-100, 100, 1):
  t = x + i
  if t < 1:
    continue
  res = Decimal(B) * Decimal(t) - Decimal(B) + Decimal(A) / ((Decimal(t)) ** (Decimal(1) / Decimal(2)))
  mr = min(mr, res)
print(mr)
