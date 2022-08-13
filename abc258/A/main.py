#!/usr/bin/env python3
K = int(input())

h = K // 60
m = K % 60

print('{:02d}:{:02d}'.format((21 + h) % 24, m))