#!/usr/bin/env python3.8
S = input()
S = S[::-1]

ans = 0
mods = [0] * 2019
mods[0] = 1
current = 0
x = 1
for s in S:
  # print('s', s)
  current = (current + x * int(s)) % 2019
  ans += mods[current % 2019]
  mods[current % 2019] += 1
  x = x * 10 % 2019
  # print('current', current)
print(mods)
print(ans)