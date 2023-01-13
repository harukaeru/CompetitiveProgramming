#!/usr/bin/env python3.8
# https://qiita.com/Kept1994/items/e9179d1dd7c6455d6883
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L) -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res

N,K=map(int, input().split())
S = input()

encoded = runLengthEncode(S)

for i in range(K):
  if len(encoded) >= 3:
    right = encoded.pop()
    mid = encoded.pop()
    left = encoded.pop()

    encoded.append((left[0], left[1] + mid[1] + right[1]))
  elif len(encoded) == 2:
    right = encoded.pop()
    mid = encoded.pop()
    encoded.append((mid[0], mid[1] + right[1]))

tot = 0
for s, v in encoded:
  tot += v - 1
print(tot)