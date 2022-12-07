#!/usr/bin/env python3.8
N = int(input())
S = input()

S = list(S)

R = ''
i = 0
b_flag = False
while i < len(S):
  if S[i] == 'C':
    if b_flag:
      R += 'B'

    R += 'C'
    b_flag = False
  elif S[i] == 'B':
    if b_flag:
      R += 'A'
      b_flag = False
    else:
      b_flag = True
  elif S[i] == 'A':
    if b_flag:
      R += 'A'
      b_flag = True
    else:
      R += 'A'
      b_flag = False
  i += 1
if b_flag:
  R += 'B'
print(R)