import sys
from collections import Counter

fin = sys.stdin
# fin = open("b.in")
fout = sys.stdout

nt = int(fin.readline())

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  u = int(fin.readline())
  c = Counter()

  d = set()

  for i in range(10000):
    q, r = fin.readline().split()
    c[r[0]] += 1
    for a in r:
      d.add(a)

  s = [pair[0] for pair in sorted(c.items(), key=lambda item: item[1], reverse = True)]
  
  for a in d:
    if a not in c:
      zero = a

  res =  zero + "".join(s)

  fout.write(res + "\n")
    