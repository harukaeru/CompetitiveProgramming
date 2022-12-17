#!/usr/bin/env python3.8
from itertools import groupby

S = input()

print(len(list(groupby(S))) - 1)