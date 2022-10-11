from decimal import Decimal, getcontext
from math import e

getcontext().prec = 400

def fp(a):
  y = Decimal(e) ** Decimal(a)
  f = Decimal(e) ** Decimal(a)

  b = y - f * Decimal(a)
  return (Decimal(2) - Decimal(b)) / Decimal(f)


a = 2
for i in range(10):
  a = fp(a)
  print(a)