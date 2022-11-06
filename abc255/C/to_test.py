#!/usr/bin/env python3.8
X, A, D, N = map(int, input().split())

def check(n):
    if A <= n <= A + N * D or A + N * D <= n <= A:
        if (n - A) % D == 0:
            return True
        else:
            return False
    return False

i = 0
while True:
    if check(X + i) or check(X - i):
        print(i)
        exit()
    i += 1
print(i)
