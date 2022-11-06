#!/usr/bin/env python3.8
import math

N, M = map(int, input().split())

*A, = map(int, input().split())

# dp = {}
#
# # count = 0
# def gcd(a, k):
#     if dp.get((a, k)):
#         # global count
#         # count += 1
#         # print(count)
#         return dp[(a, k)]
#     if dp.get((k, a)):
#         # global count
#         # count += 1
#         # print(count)
#         return dp[(k, a)]
#
#
#     if k == 1:
#         dp[(a, k)] = k
#         return 1
#
#     r = a % k
#     if r == 0:
#         dp[(a, k)] = k
#         return k
#
#     o = gcd(k, r)
#     dp[(a, k)] = o
#     return o

fl = [True] * M  #
# S = list(range(1, M+1))

def pfact(num):
    factorials = []

    i = 2
    while i * i <= num:
        while(num % i == 0):
            num = int(num / i)
            factorials.append(i)
            # print('num', num)
        i += 1
    if num != 1:
        factorials.append(num)
    return factorials

for a in A:
    v = pfact(a)
    # print('v', v)
    for nx in v:
        if fl[nx - 1]:
            for i in range(nx, M + 1, nx):
                # print('i', i)
                fl[i - 1] = False
            # print(fl)

out = []
for i, flag in enumerate(fl):
    if flag:
        out.append(i + 1)

# print('fl', fl)
print(len(out))
for o in out:
    print(o)
