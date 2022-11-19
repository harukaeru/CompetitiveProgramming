#!/usr/bin/env python3.8
X = input()

if X == '':
  print('YES')
  exit()


while X:
  can_continue = False
  for k in ['ch', 'o', 'k', 'u']:
    if X.startswith(k):
      X = X[len(k):]
      can_continue = True
      break

  if X == '':
    print('YES')
    exit()
  
  if not can_continue:
    print('NO')
    exit()