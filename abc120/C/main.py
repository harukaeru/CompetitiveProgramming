#!/usr/bin/env python3.8
S = input()

print(min(S.count('0'), S.count('1')) * 2)