N = int(input())
*A, = map(int, input().split())

count = 0
while 1:
    is_all_even = True
    A_mapped = []
    for a in A:
        if a % 2 != 0:
            is_all_even = False
            break
        A_mapped.append(int(a / 2))

    if is_all_even:
        count += 1
        A = A_mapped
    else:
        break

print(count)
