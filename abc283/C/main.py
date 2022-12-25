#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)
S = input()

S = S.replace('00', 'a')
print(len(S))