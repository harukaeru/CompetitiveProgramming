import sys

def generate_key(p, q):
  n = p * q
  phi = (p - 1) * (q - 1)

  def extgcd(a, b):
    if b == 0:
      return a, 1, 0
    d, y, x = extgcd(b, a % b)
    y -= (a // b) * x
    return d, x, y

  def create_secret_key(pub, phi):
    d, x, y = extgcd(phi, pub)
    y = y % phi
    return y
  
  e = 65537
  return str(e) + '_' + str(n), str(create_secret_key(e, phi)) + '_' + str(n)

def encrypt(mes, public_key):
  e, n = map(int, public_key.split('_'))
  return (mes ** e) % n

def decrypt(mes, secret_key):
  d, n = map(int, secret_key.split('_'))
  return (mes ** d) % n

if __name__ == '__main__':
  if sys.argv[1] == 'generate':
    p = int(sys.argv[2])
    q = int(sys.argv[3])
    keys = generate_key(p, q)
    print('---------pub---------')
    print(keys[0])
    print('---------sec---------')
    print(keys[1])
  elif sys.argv[1] == 'encrypt':
    pub = sys.argv[2]
    mes = sys.argv[3]
    fom = ''.join(['{0:>02s}'.format(hex(ord(x)).replace('0x', '')) for x in mes])
    fom = int('0x' + fom, 16)

    print(hex(encrypt(fom, pub)))
  elif sys.argv[1] == 'decrypt':
    sec = sys.argv[2]
    mes = int(sys.argv[3], 16)

    fom = decrypt(mes, sec)
    fom = hex(fom).replace('0x', '')
    fom = '0' + fom if len(fom) % 2 != 0 else fom
    dec = ''
    for i in range(0, len(fom), 2):
      dec += chr(int('0x' + str(fom[i]) + str(fom[i+1]), 16))
    print(dec)
  else:
    raise Exception