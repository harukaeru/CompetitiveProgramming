#!/usr/bin/env python3
S = input()

K = list(range(10))
ng_list = set()
required_list = []
for i, s in enumerate(S):
    if s == 'x':
        ng_list.add(i)
    elif s == 'o':
        required_list.append(i)

ans = 0
for key in range(10000):
    k1 = key % 10
    k2 = (key % 100) // 10
    k3 = (key % 1000) // 100
    k4 = (key % 10000) // 1000

    if (k1 in ng_list) or (k2 in ng_list) or (k3 in ng_list) or (k4 in ng_list):
        continue

    has_all_required = True
    data = [k1, k2, k3, k4]
    for r in required_list:
        if r not in data:
            has_all_required = False
    if not has_all_required:
        continue

    # print(k1, k2, k3, k4)

    ans += 1

print(ans)
