import sys

fin = sys.stdin
# fin = open("b.in")
fout = sys.stdout

nt = int(fin.readline())

INF = 999999

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  v, e = (int(x) for x in fin.readline().split())
  order = [0] + [-int(x) for x in fin.readline().split()]
  a = [[] for i in range(v)]
  edges = dict()
  res = [0] * e
  for i in range(e):
    v1, v2 = (int(x)-1 for x in fin.readline().split())
    a[v1].append(v2)
    a[v2].append(v1)
    edges[ (v1, v2) ] = i
    edges[ (v2, v1) ] = i

  for i in range(1, v):
    for tv in range(v):
      if order[tv] == i:
        for adj_v in a[tv]:
          if order[adj_v] <= i:
            res[ edges[ (tv, adj_v) ] ] = max(i - order[adj_v], 1)

  fout.write(" ".join([str(x) for x in res]) + "\n")
    