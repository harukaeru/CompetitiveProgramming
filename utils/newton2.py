from decimal import Decimal, getcontext

getcontext().prec = 400

def fp(a):
  y = Decimal(a) * Decimal(a) * Decimal(a)

  f = Decimal(3) * Decimal(a) * Decimal(a)
  b = y - f * Decimal(a)
  return (Decimal(2) - Decimal(b)) / Decimal(f)


a = 2
for i in range(10):
  a = fp(a)
  print(a)