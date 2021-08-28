import sys

n = int(sys.stdin.readline())

def include_3(i):
    x = i
    # print('i', i)
    while x:
        if x % 10 == 3:
            print(f' {i}', end='')
            break
        x = x // 10


for i in range(1, n + 1):
    if i % 3 == 0:
        print(f' {i}', end='')
        continue
    else:
        include_3(i)
print()
