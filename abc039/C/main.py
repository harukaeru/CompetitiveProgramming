#!/usr/bin/env python3.8
S = input()

k = 'WBWBWWBWBWBW'
k = k * 3

i = k.index(S)
ranks = {
  0: 'Do', 
  2: 'Re', 
  4: 'Mi', 
  5: 'Fa',
  7: 'So',
  9: 'La',
  11: 'Si'
}

pos = None
for i in range(0, 13):
  l = k[i:len(S) + i]
  if S == l:
    pos = i
    break

print(ranks[pos])