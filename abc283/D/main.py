#!/usr/bin/env pypy3
from collections import Counter
import sys
sys.setrecursionlimit(300000)


S = input()

stacks = []
box = Counter()

i = 0
while i < len(S):
  # print('i', i)
  chars = Counter()
  stacks.append(chars)

  while len(stacks) > 0:
    chars = stacks[-1]
    while i < len(S):
      # print('stacks', i, '->', stacks)
      # print(stacks)
      if S[i] == '(':
        i += 1
        stacks.append(Counter())
        chars = stacks[-1]
        continue
      if S[i] == ')':
        i += 1
        box -= chars
        stacks.pop()
        break

      for k, v in box.items():
        if v >= 1 and k == S[i]:
          print('No')
          exit()
      chars[S[i]] += 1
      box[S[i]] += 1
      i += 1
    
    if i == len(S):
      break
    
  i += 1

print('Yes')