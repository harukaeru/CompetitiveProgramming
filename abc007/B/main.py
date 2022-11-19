#!/usr/bin/env python3.8
A = input()

if A == 'a':
  print(-1)
  exit()

if len(A) == 1:
  print(chr(ord(A) - 1))
  exit()

print(A[:len(A)-1])