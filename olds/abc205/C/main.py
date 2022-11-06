#!/usr/bin/env python3.8
A, B, C = map(int, input().split())

# def pow(x, y):
#     # print('x,y', x, y)
#     ans = 1
#     while y:
#         if y % 2 != 0:
#             ans *= x
#             y -= 1
#         y //= 2
#         print('y', y)
#         x *= x
#         # print('x', x)
#     return ans
#     # print('ans', ans)
#     # return ans * pow(x ** 2, y)

if C % 2 == 0:
    absa = abs(A)
    absb = abs(B)
    if absa > absb:
        print('>')
    elif absa == absb:
        print('=')
    else:
        print('<')
else:
    if A < B:
        print('<')
    elif A == B:
        print('=')
    else:
        print('>')
