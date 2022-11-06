#!/usr/bin/env python3.8

arrays = []
for __ in range(3):
    *a, = map(int, input().split())
    arrays.append(a)

# a1, a2, a3, b1, b2, b3

for a1 in range(101):
   b1_1 = arrays[0][0] - a1  # c11
   b2_1 = arrays[0][1] - a1  # c12
   b3_1 = arrays[0][2] - a1  # c13
   if not (0 <= b1_1 <= 100 and 0 <= b2_1 <= 100 and 0 <= b3_1 <= 100):
       continue
   for a2 in range(101):
        b1_2 = arrays[1][0] - a2
        b2_2 = arrays[1][1] - a2
        b3_2 = arrays[1][2] - a2

        if not (0 <= b1_2 <= 100 and 0 <= b2_2 <= 100 and 0 <= b3_2 <= 100):
            continue
        for a3 in range(101):
            b1_3 = arrays[2][0] - a3
            b2_3 = arrays[2][1] - a3
            b3_3 = arrays[2][2] - a3
            if not (0 <= b1_3 <= 100 and 0 <= b2_3 <= 100 and 0 <= b3_3 <= 100):
             continue
            if (b1_1 == b1_2) and (b1_1 == b1_3) and (b2_1 == b2_2) and (b2_1 == b2_3) and (b3_1 == b3_2) and (b3_1 == b3_3):
                # print(a1, a2, a3, b1_1, b2_1, b3_1)
                print('Yes')
                exit()

print('No')
