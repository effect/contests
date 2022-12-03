def sqr(x):
	return x * x

with open("a.in") as fin, open("a.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")
		INF = 1000000000

		n, m = (int(s) for s in fin.readline().split())
		a = [0] * n
		for i in range(n):
			a[i] = [int(x) for x in fin.readline().split()]
			a[i].sort()
		res = 0
		if m < n:
			for i in range(n):
				a[i] += [INF] * (n - m)

		d = [[INF] * n for _ in range(n)]

		s = 0
		for i in range(n):
			s += a[0][i]
			d[0][i] = s + sqr(i + 1)

		for i in range(1, n):
			for j in range(i, n):
				d[i][j] = d[i - 1][j]
				s = 0
				for k in range(1, j - i + 2):
					s += a[i][k - 1]
					cur = d[i - 1][j - k] + s + sqr(k + 1)
					d[i][j] = min(d[i][j], cur)

		print a
		print d

		res = d[-1][-1]

		fout.write(str(res))
		fout.write("\n")