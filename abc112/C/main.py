#!/usr/bin/env python3
N = int(input())

arrays = []
special_i = None
for i in range(N):
    x_i, y_i, h_i = map(int, input().split())
    arrays.append((x_i, y_i, h_i))
    if h_i >= 1:
        special_i = i

ans = []
for c_x in range(101):
    for c_y in range(101):
        x_0, y_0, h_0 = arrays[special_i]
        H = h_0 + abs(x_0 - c_x) + abs(y_0 - c_y)
        H = max(H, 0)

        ok = True
        for x_i, y_i, h_i in arrays:
            h_req = H - abs(x_i - c_x) - abs(y_i - c_y)
            h_req = max(h_req, 0)
            if h_i != h_req:
                ok = False
        if ok:
            ans.append([c_x, c_y, H])

if len(ans) == 1:
    print(' '.join(list(map(str, ans[0]))))

# for i in range(N):
# h_1 = H - (dx + dy)

 # if h_1 + dx + dy < 0:
#  H = h_1 + dx + dy
#
# h_i = max(H - dx - dy, 0)
# h_i + dx + dy =
