#!/usr/bin/env python3.8
S = input()

tot = 0
for i in range(2 ** (len(S) - 1)):
  s = ''
  for j in range(len(S) - 1):
    s += S[j]
    if i & (1 << j) != 0:
      s += '+'
  
  s += S[-1]

  tot += eval(s)
      
  # print(s)
print(tot)