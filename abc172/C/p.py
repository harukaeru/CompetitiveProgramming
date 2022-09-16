import bisect

a = [0, 9, 12, 14, 15, 20, 21]
print(bisect.bisect_right(a, 1))
bisect.insort_left(a, 1)
print(a)
