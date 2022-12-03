import sys
from operator import itemgetter

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

def cuts_number(a, index, k, d):
  # x = a[index] / k
  cuts = 0
  used = [False] * (len(a) - index)
  for i in range(index, len(a)):
    if d <= 0:
      break
    if (a[i] * k) % a[index] == 0:
      pcs = a[i] * k // a[index]
      if pcs <= d:
        d -= pcs
        used[i - index] = True
        cuts += pcs - 1
  
  if d > 0:
    for i in range(index, len(a)):
      if not used[i - index]:
        pcs = (a[i] * k) // a[index]
        pcs = min(pcs, d)
        d -= pcs
        cuts += pcs
        if d <= 0:
          break
  if d > 0:
    return -1
  return cuts


for tn in range(nt):
    fout.write("Case #" + str(tn + 1) + ": ")
    n, d = (int(x) for x in fin.readline().split())
    a = [int(x) for x in fin.readline().split()]

    res = d - 1
    a.sort()

    k = 1
    while k - 1 < res:
      for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
          continue
        cuts = cuts_number(a, i, k, d)
        # print(k, i, cuts)
        if cuts >= 0:
          res = min(res, cuts)
      k += 1

    fout.write(str(res))
    fout.write('\n')
    