#!/usr/bin/env python3
import math
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

print(sum(map(lambda x: math.comb(x, 2), counter.values())))
