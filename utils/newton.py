from decimal import Decimal, getcontext

getcontext().prec = 400

def fp(a):
  x = (Decimal(2) + Decimal(a) * Decimal(a)) / (Decimal(2) * Decimal(a))
  return x


a = 2
for i in range(10):
  a = fp(a)
  print(a)