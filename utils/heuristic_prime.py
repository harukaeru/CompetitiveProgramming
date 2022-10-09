import numpy as np
from matplotlib import pyplot as plt

def generate_primes(N):
  primes = [True] * (N + 1)
  primes[0] = False
  primes[1] = False

  results = []
  for p, is_prime in enumerate(primes):
    if not is_prime:
      continue
    results.append(p)

    for xp in range(2 * p, N + 1, p):
      primes[xp] = False
  
  return results

nine_nine_but_over_9 = set()
for i in range(2, 10):
  for j in range(2, 10):
    if i * j > 9:
      nine_nine_but_over_9.add(i * j)

instant_ok = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
instant_ng = set([121, 169])
def evaluate(n):
  if n in instant_ok:
    return True

  if n % 2 == 0:
    return False
  
  if str(n)[-1] == '5':
    return False
  
  if n % 3 == 0:
    return False
  
  if n in nine_nine_but_over_9:
    return False

  if n in instant_ng:
    return False
  
  if n % 7 == 0:
    return False

  return True

def test(N):
  N = int(N)
  real_primes = set(generate_primes(N))
  heur_primes = set([i for i in range(2, N + 1) if evaluate(i)])
  
  print('-----', N, '-----')
  print('素数っぽいとみなした個数:', len(heur_primes))
  print('外した個数:', len(heur_primes) - len(real_primes), '誤答率:', 1 - len(real_primes) / len(heur_primes))
  print('素数の個数:', len(real_primes),'正答率:', len(real_primes) / len(heur_primes))
  print()
  r = (len(real_primes) / len(heur_primes)) * 100
  return r

x = np.arange(1, 7, 0.1)
vtest = np.vectorize(test)
y = vtest(10 ** x)

plt.plot(x, y)
plt.xlabel('number(10^x)')
plt.ylabel('Accuracy(%)')

plt.show()