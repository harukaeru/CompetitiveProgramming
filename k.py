LIMIT = 100

t = 0
completed = False
should = True
if should:
  while(not completed):
    print('x')

    t += 1
    if t == LIMIT:
      break
  print(t)
