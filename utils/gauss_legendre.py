import math
from decimal import Decimal, getcontext

getcontext().prec = 330

a = Decimal(1)
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = Decimal(1)

M = 10
for i in range(M):
  a_nex = (a + b) / Decimal(2)
  b_nex = (a * b).sqrt()
  t_nex = t - p * (a - a_nex) * (a - a_nex)
  p_nex = Decimal(2) * p

  a = a_nex
  b = b_nex
  t = t_nex
  p = p_nex
  print(f'{i: 3d}', ':', (a + b) * (a + b) / (Decimal(4) * t))