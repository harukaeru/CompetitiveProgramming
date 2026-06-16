#!/usr/bin/env python3.8
rep = int(input())

total_gifts = []
for i in range(rep):
  total_gifts.append([])
for i in range(rep):
  giftees = list(map(int, input().split()))[1:]
  for giftee in giftees:
    total_gifts[giftee - 1].append(i + 1)

for gifts in total_gifts:
  print(len(gifts), end='')
  if gifts:
    print(' ', end='')
    print(' '.join(map(str, gifts)))
  else:
    print()