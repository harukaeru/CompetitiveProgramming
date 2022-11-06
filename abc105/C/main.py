#!/usr/bin/env python3.8
N = int(input())

ss = []
while N != 0:
  if N > 0:
    s = N % 2 
    ss.append(s)

    N = -(N // 2)
    # print('u:', N)
  else:
    if N % 2 == 1:
      p = abs(N) + 2
      s = p % 2
      ss.append(s)
      N = p // 2
      # print('l:', N)
    else:
      ss.append(0)
      N = abs(N) // 2
      # print('p', N)

ss.reverse()
if ss:
  print(''.join(map(str, ss)))
else:
  print(0)