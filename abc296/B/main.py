#!/usr/bin/env python3.8
S = []
for i in range(8):
  S.append(input())

for j in range(8):
  for i in range(8):
    if S[i][j] == '*':
      print(chr(ord('a') + j) + str(7 - i + 1))
      break
