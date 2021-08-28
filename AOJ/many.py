S, T = [int(n) for n in input().replace('\n', '').split()]

count = 0
for a in range(S + 1):
    for b in range(S + 1):
        if S - (a + b) < 0:
            break

        if a == 0:
            count += (S + 1)
            break
        if b == 0:
            count += (S + 1)
            continue

        for c in range(S + 1):
            if a + b + c <= S and a * b * c <= T:
                count += 1

print(count)
