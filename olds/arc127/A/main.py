#!/usr/bin/env python3.8
N = int(input())

def get_all(sn):
    k = len(sn)
    s = 0
    while k > 0:
        s += int('1' * k)
        k -= 1
    return s

sn = str(N)
k = len(str(N))
i = 0
c = 0
while i < k:
    if int(sn[i]) >= 1:
        print('i', i, 10 ** (k - i - 1))
        c += 10 ** (k - i - 1)
    else:
        break

    i += 1
print('c', c)
# def f(sn):
#     print('sn', sn)
#     sn0 = int(sn[0])
#     if len(sn) == 1 and sn0 >= 1:
#         print('ケース1', 1)
#         return 1
#     if len(sn) == 1 and sn0 == 0:
#         return 0
#
#     if sn0 >= 2:
#         # count = 10 ** (len(sn) - 1)
#         # print('sn0>=2', count + f(sn[1:]) * 2)
#         x = get_all(sn)
#         print('sn0==2:x', x)
#         return x
#     elif sn0 == 1:
#         a = 10 ** (len(sn) - 1)
#         count = int(sn) - a + 1
#         print('count', count)
#         x = count + f(sn[1:]) * 2
#         print('sn0==1:x', x)
#         return x
#     elif sn0 == 0:
#         return f(sn[1:]) * 2

