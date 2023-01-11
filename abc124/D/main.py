#!/usr/bin/env python3.8
from collections import deque
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


N, K = map(int, input().split())
S = input()

# print(runLengthEncode(S))
rle = runLengthEncode(S)

tot = 0
r = 0
l = 0
zero_cnt = 0
ans = 0
while r < len(rle):
  tot += rle[r][1]
  if rle[r][0] == '0':
    zero_cnt += 1

  while K < zero_cnt:
    tot -= rle[l][1]
    if rle[l][0] == '0':
      zero_cnt -= 1
    l += 1
  ans = max(ans, tot)

  r += 1

print(ans)