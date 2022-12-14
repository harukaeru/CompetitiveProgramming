#!/usr/bin/env python3.8
x = int(input())
cnt = x // 11
rest = x % 11

rest = 0 if rest == 0 else (2 if rest > 6 else 1)

print(cnt * 2 + rest)