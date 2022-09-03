#!/usr/bin/env python3
import math
N, K = map(int, input().split())

rest = N % K
print(min(rest, abs(rest - K)))