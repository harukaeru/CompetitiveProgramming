from decimal import Decimal
p = 1
s = 0
while s <= 30:
  s += Decimal(1) / Decimal(p)
  p += 1
  print('s', s)

print(s)
