#!/usr/bin/env python3.8
N = int(input())
S = input()


a = any(['o' == S[i] for i in range(N)])
b = all(['x' != S[i] for i in range(N)])
if a and b:
  print('Yes')
else:
  print('No')