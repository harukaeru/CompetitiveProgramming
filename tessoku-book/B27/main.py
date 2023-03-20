#!/usr/bin/env python3.8
import math


A,B=map(int, input().split())
print(A * B // math.gcd(A, B))