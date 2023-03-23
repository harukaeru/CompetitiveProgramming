#!/usr/bin/env python3.8
N = int(input())

c3 = N // 3
c5 = N // 5
c7 = N // 7

c15 = N // 15
c21 = N // 21
c35 = N // 35

c105 = N // 105

print(c3 + c5 + c7 - (c15 + c21 + c35) + c105)