import sys

fin = sys.stdin
fout = sys.stdout

nt = int(fin.readline())

def trace(a):
	sum = 0
	for i in range(len(a)):
		sum += a[i][i]
	return sum

def has_duplicates(row):
	cnt = [0] * (len(row) + 1)
	for x in row:
		cnt[x] += 1
		if cnt[x] > 1:
			return 1
	return 0

for tn in range(nt):
  fout.write("Case #" + str(tn + 1) + ": ")

  n = int(fin.readline())
  a = []
  for i in range(n):
  	a.append([int(x) for x in fin.readline().split()])
  
  r = sum(has_duplicates(a[i]) for i in range(n))
  c = sum(has_duplicates([a[j][i] for j in range(n)]) for i in range(n))

  fout.write(" ".join([str(x) for x in (trace(a), r, c)]))
  fout.write('\n')
    