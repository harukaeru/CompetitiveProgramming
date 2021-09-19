#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
S = input()

dp = {
    'c': 0,
    'h': 0,
    'o': 0,
    'k': 0,
    'u': 0,
    'd': 0,
    'a': 0,
    'i': 0,
}

for i, s in enumerate(S):
    if s == 'c':
        dp['c'] = dp['c'] + 1
    if s == 'h':
        dp['h'] += dp['c']
    if s == 'o':
        dp['o'] += dp['h']
    if s == 'k':
        dp['k'] += dp['o']
    if s == 'u':
        dp['u'] += dp['k']
    if s == 'd':
        dp['d'] += dp['u']
    if s == 'a':
        dp['a'] += dp['d']
    if s == 'i':
        dp['i'] += dp['a']
print(dp['i'] % MOD)
