#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

absa = [abs(a) for a in A]
minus_count = len([a for a in A if a < 0])
if minus_count % 2 == 0:
  print(sum(absa))
else:
  print(sum(absa) - 2 * min(absa))
