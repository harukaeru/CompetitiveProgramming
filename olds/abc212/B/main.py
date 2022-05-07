#!/usr/bin/env python3

XXXX = input().replace('\n', '')


if len(set(XXXX)) == 1:
    print('Weak')
    exit()

current = -1
ladder_count = 0

for i, x in enumerate(XXXX):
    x = int(x)

    if i == 0:
        current = x
        continue

    if (current + 1) % 10 == x:
        ladder_count += 1
        current = x

if ladder_count == 3:
    print("Weak")
    exit()

print('Strong')
