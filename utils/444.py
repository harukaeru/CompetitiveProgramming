from decimal import Decimal
p = 1
s = 0
while s <= 30:
  s += 1.0 / p
  p += 1

print(s)
