import sys
from math import sqrt

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

EPS = 1e-10

def get_max_even_first(k, value):
  return int(k - sqrt(k*k + 4*value) + EPS)

def get_max_even_second(k, value):
  return int( -(k+1) + sqrt( (k+1)*(k+1) + 4*value ) + EPS)

def get_max_odd_first(k, value):
  return get_max_even_first(k, value) - 1

def get_max_odd_second(k, value):
  return get_max_even_second(k, value) + 1

def get_from_first(k, n):
  if n % 2 == 0:
    return k * n // 2 + (n // 2) * (n // 2)
  else:
    return k * (n + 1) // 2 + ((n + 1) // 2) * ((n + 1) // 2)

def get_from_second(k, n):
  if n % 2 == 0:
    return k * n // 2 + (n // 2) * (n // 2 + 1)
  else:
    return k * (n // 2) + (n // 2) * ((n + 1) // 2)

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  l, r = (int(x) for x in fin.readline().split())

  diff = abs(l - r)
  k = int( (sqrt(1 + 8 * diff) - 1) / 2 + EPS)
  if l >= r:
    l -= k * (k + 1) // 2
  else:
    r -= k * (k + 1) // 2

  start_l = (l >= r)

  # print(diff)
  # print(k)
  # print(l, r)

  if start_l:
    first = l
    second = r
  else:
    first = r
    second = l

  # print(start_l)

  n1 = get_max_even_first(k, first)
  n2 = get_max_even_second(k, second)

  max_even_n = max(n1, n2)

  n1 = get_max_odd_first(k, first)
  n2 = get_max_odd_second(k, second)

  max_odd_n = max(n1, n2)

  max_n = 0
  for test in range(max(0, min(max_odd_n, max_even_n)-5), max(max_even_n, max_odd_n) + 5):
    # print(test)
    from_first = get_from_first(k, test)
    from_second = get_from_second(k, test)
    # print(from_first ,from_second)
    if (first >= from_first) and (second >= from_second):
      max_n = test

  res = max_n + k

  n = max_n

  if start_l:
    l -= get_from_first(k, n)
    r -= get_from_second(k, n)
  else:
    r -= get_from_first(k, n)
    l -= get_from_second(k, n)

  fout.write(" ".join([str(res), str(l), str(r)]) + "\n")