import sys
import math

for line in sys.stdin:
    a, op, b = line.split(' ')
    if op == '?':
        exit()
    a, b = int(a), int(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)
