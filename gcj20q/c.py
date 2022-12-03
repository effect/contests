import sys
from operator import itemgetter

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

def letter(c):
  if c == 0:
    return "C"
  return "J"


for tn in range(nt):
    fout.write("Case #" + str(tn + 1) + ": ")
    n = int(fin.readline())

    w = []
    for i in range(n):
      a, b = [int(x) for x in fin.readline().split()]
      w.append([a, b, i, 0, 0])
    w = sorted(w, key=itemgetter(0))

    fail = False
    inters = [w[0]]
    for i in range(1, n):
      cur = w[i]
      for j in inters:
        if cur[0] >= j[1]:  # doesn't overlap
          j[4] = 1  # mark for removal
        else:  # overlap
          cur[3] = 1 - j[3]  # set opposite color
      inters.append(cur)

      inters = [s for s in inters if (s[4] == 0)]
      if len(inters) > 2:
        fail = True
        break

    if fail:
      res = "IMPOSSIBLE"
    else:
      w = sorted(w, key=itemgetter(2))
      res = "".join([letter(x[3]) for x in w])

    fout.write("".join(res))
    fout.write('\n')
    