#!/usr/bin/env python3
N, A, B, C = map(int, input().split())
L = []
for i in range(N):
  L.append(int(input()))

min_point = 9999999999
for i in range(4 ** N + 1):
  point = 0
  stores = [0, 0, 0]
  q = i
  for j in range(N):
    address = q % 4 
    if address == 3:
      pass
    elif stores[address] != 0:
      stores[address] += L[j]
      point += 10
    else:
      stores[address] += L[j]
    q //= 4
  
  if any([s == 0 for s in stores]):
    continue
  point += abs(stores[0] - A)
  point += abs(stores[1] - B)
  point += abs(stores[2] - C)
  # print(i, '->', point)
  min_point = min(min_point, point)
  # if min_point > point:
  #   min_point = min(min_point, point)
  #   q = i
  #   addresses = []
  #   for j in range(N):
  #     addresses.append(q % 4)
  #     q //= 4
  #   print(addresses, min_point)


print(min_point)