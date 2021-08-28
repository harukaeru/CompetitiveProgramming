import sys

def check(line):
    W, H, x, y, r = [int(n) for n in line.split(' ')]

    is_over = (x + r) > W or (x - r) < 0 or (y + r) > H or (y - r) < 0
    if is_over:
        print('No')
        return
    print('Yes')

for line in sys.stdin:
    check(line)
