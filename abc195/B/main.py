#!/usr/bin/env python3.8
A, B, W = map(int, input().split())

mi = -1
ma = -1
# もっとも少ない個数
min_count = W * 1000 // B
# 一致すればそのまま。一致しなければ足りないのでそれより1個多いハズ
if min_count == W * 1000 / B:
  mi = min_count
else:
  mi = min_count + 1

max_count = W * 1000 // A
# 一致すればそのまま。一致しなくてもその個数まで実数を駆使して小さくすればいい
if max_count == W * 1000 / A:
  ma = max_count
else:
  ma = max_count

if (mi > ma):
  print('UNSATISFIABLE')
  exit()

print(mi, ma)