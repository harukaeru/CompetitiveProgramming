#!/usr/bin/env python3.8
s = input()

a = s.index('A')
t = s[::-1]
b = t.index('Z')
b = len(s) - b - 1

print(b - a + 1)