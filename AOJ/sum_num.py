import sys

for line in sys.stdin:
    line = line.replace('\n', '')
    if line == '0':
        exit()

    s = 0
    for i in line:
        s += int(i)
    print(s)
