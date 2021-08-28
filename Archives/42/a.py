x = map(int, input().split())

five_count = 0
seven_count = 0
for i in x:
    if i == 5:
        five_count += 1
    elif i == 7:
        seven_count += 1

if five_count == 2 and seven_count == 1:
    print('YES')
else:
    print('NO')
