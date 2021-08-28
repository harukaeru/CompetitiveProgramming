import sys

for line in sys.stdin:
    m, f, r = [int(n) for n in line.replace('\n', '').split(' ')]
    if m == -1 and f == -1 and r == -1:
        break

    if m == -1 or f == -1:
        print('F')
        continue

    if m + f >= 80:
        print('A')
        continue

    if m + f >= 65:
        print('B')
        continue

    if m + f >= 50:
        print('C')
        continue

    if m + f >= 30:
        if r >= 50:
            print('C')
            continue
        print('D')
        continue

    if m + f < 30:
        print('F')
        continue

    raise Exception('Not defined')
