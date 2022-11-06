#!/usr/bin/env python3.8
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

print(counter[100] * counter[400] + counter[200] * counter[300])