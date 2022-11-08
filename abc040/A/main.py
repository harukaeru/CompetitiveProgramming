#!/usr/bin/env python3.8
n,x= map(int, input().split())
print(min(x - 1, n - x))