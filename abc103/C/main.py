#!/usr/bin/env python3
N = int(input())
a = list(map(int, input().split()))

s = sum([x - 1 for x in a])

print(s)