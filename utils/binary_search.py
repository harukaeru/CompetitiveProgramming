N = [1, 4, 5, 12, 15, 20, 22, 23]

ng = len(N)
ok = -1

while ng - ok > 1:
  mid = (ng + ok) // 2
  is_ok = N[mid] > 7 and N[mid] % 2 == 0

  if is_ok:
    ok = mid
  else:
    ng = mid

if ok == -1:
  print('Not found')
else:
  print(ok, '->', N[ok])