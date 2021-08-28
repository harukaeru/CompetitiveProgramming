import sys

for line in sys.stdin:
    n, x = [int(n) for n in line.replace('\n', '').split(' ')]
    if n == 0 and x == 0:
        break

    n_list = list(range(1, n + 1))

    count = 0
    for i in range(len(n_list) - 2):
        a = n_list[i]
        for j in range(i + 1, len(n_list) -1):
            b = n_list[j]
            for k in range(j + 1, len(n_list)):
                c = n_list[k]
                if a + b + c == x:
                    count += 1
    print(count)
