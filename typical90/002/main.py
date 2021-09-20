#!/usr/bin/env python3
N = int(input())
if N % 2 != 0:
    print()
    exit()

def validate(inp):
    if inp.count('0') != inp.count('1'):
        return False
    stacks = []
    for s in inp:
        if s == '0':
            stacks.append(s)
        elif s == '1':
            if len(stacks) == 0:
                return False
            stacks.pop()
    return True

L = 2 ** N
m = L - 1
fo = '{i:0>' + str(N) + '}'

rows = []
for i in range(L):
    s = str(bin(i)).replace('0b', '')
    s = fo.format(i=s)
    if validate(s):
        print(s.replace('0', '(').replace('1', ')'))
