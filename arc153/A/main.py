#!/usr/bin/env python3.8
N = int(input())
a,b,c,d,e,f = str(N + 100000 - 1)
print(''.join([a,a,b,c,d,d,e,f,e]))