#!/usr/bin/env python3.8
N = int(input())
S = input()

i = 0
ret = ''
while i < N:
  ret += S[i].replace(',', '.')
  if S[i] == '"':
    i += 1
    while S[i] != '"':
      ret += S[i]
      i += 1
    ret += '"'

  i += 1

print(ret) 