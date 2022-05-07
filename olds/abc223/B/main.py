#!/usr/bin/env python3
S = input()

s = list(S)

all_s = []

for i in range(len(s)):
    n = s[i:] + s[:i]
    all_s.append(''.join(n))

print(min(all_s))
print(max(all_s))
