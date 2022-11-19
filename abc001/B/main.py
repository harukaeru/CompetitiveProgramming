#!/usr/bin/env python3.8
m = int(input())

k1 = m // 100
k = m // 1000

if k1 == 0:
  print('00')
elif k1 <= 50:
  print(f'{k1 % 100:02d}')
elif k <= 30:
  print(f'{k % 100 + 50:02d}')
elif k <= 70 and m <= 70000:
  print(f'{(k - 30) // 5 + 80:02d}')
else:
  print(89)