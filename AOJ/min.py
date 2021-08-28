import sys
import math

length = int(sys.stdin.readline())
array = [int(n) for n in sys.stdin.readline().split(' ')]

min_num = array[0]
max_num = array[0]
sum_num = 0

for i in range(len(array)):
    if min_num > array[i]:
        min_num = array[i]
    if max_num < array[i]:
        max_num = array[i]
    sum_num += array[i]

print(min_num, max_num, sum_num)
