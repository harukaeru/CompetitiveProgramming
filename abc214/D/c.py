def loop(n):
    if n == 0:
      return 0

    a = loop(n - 1) + 1
    return a

print(loop(10))

