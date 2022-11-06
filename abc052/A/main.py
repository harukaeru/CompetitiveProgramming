#!/usr/bin/env python3.8
A,B,C,D = map(int, input().split())

S = A *B
P = C*D
print(max(S,P))