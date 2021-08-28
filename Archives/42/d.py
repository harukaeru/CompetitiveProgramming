H, W, A, B = map(int, input().split())

# H[0 + 1] = 1
# W[0 + 1] = 1

# (H, W) = (0, 0)
# (H, W) = (1, 0) X
# (H, W) = (0, 1)

h_w_list = [Point(0, 0)]
class Point:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __add__(self, t):
        self.h += t[0]
        self.w += t[1]

    def __repr__(self):
        return f'({self.h}, {self.w})'

for i in range(H):
    for j in range(W):
        p = starting_point + (i, j)
        if p.h >= (H - A) or p.w >= (W - B):
            continue

for i in range(W):
    q = starting_point + (0, i)
    if q.h >= (H - A) or q.w >= (W - B):
        continue

# わからん。たぶん動的計画法とかいうのを使う
