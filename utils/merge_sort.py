A = [12, 8, 2, 7, 9, 11, 211, 40, 5, 7]

def merge_sort(ary):
  if len(ary) == 1:
    return ary

  mid = len(ary) // 2

  x = merge_sort(ary[:mid])
  y = merge_sort(ary[mid:])
  z = []
  i_x = 0
  i_y = 0
  while i_x < len(x) or i_y < len(y):
    if i_x == len(x):
      z.append(y[i_y])
      i_y += 1
    elif i_y == len(y):
      z.append(x[i_x])
      i_x += 1
    elif x[i_x] <= y[i_y]:
      z.append(x[i_x])
      i_x += 1
    else:
      z.append(y[i_y])
      i_y += 1
  return z
    

print(merge_sort(A))