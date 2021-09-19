X = 2
Y = 3
W = (X + 1) * (Y + 1)
for j in range(W):
    ma = j // (Y + 1)
    mb = j % (Y + 1)
    print('m = (', ma, mb, ')')

