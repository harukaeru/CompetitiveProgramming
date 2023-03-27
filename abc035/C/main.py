#!/usr/bin/env python3.8
import itertools


N,Q=map(int, input().split())
states = [0] * (N + 1)
for i in range(Q):
  l,r=map(int, input().split())
  states[l - 1] += 1
  states[r] -= 1

states = list(itertools.accumulate(states))


states = [str(s % 2) for s in states][:N]
print(''.join(states))



