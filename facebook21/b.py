INF = 1000000

with open("b.in") as fin, open("b.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")
		
		n = int(fin.readline())
		a = [0] * n
		for i in range(n):
			a[i] = fin.readline()

		c0 = [0] * n
		cX = [0] * n
		r0 = [0] * n
		rX = [0] * n

		for i in range(n):
			for j in range(n):
				if a[i][j] == 'O':
					r0[i] += 1
					c0[j] += 1
				elif a[i][j] == 'X':
					rX[i] += 1
					cX[j] += 1

		minX = INF
		rWinX = [INF] * n
		cWinX = [INF] * n
		for i in range(n):
			if r0[i] == 0:
				rWinX[i] = n - rX[i]
				minX = min(minX, rWinX[i])
			if c0[i] == 0:
				cWinX[i] = n - cX[i]
				minX = min(minX, cWinX[i])

		# print(rWinX)
		# print(cWinX)

		if minX < INF:
			fout.write(str(minX) + " ")

			num_ways = 0
			for i in range(n):
				if rWinX[i] == minX:
					num_ways += 1
				if cWinX[i] == minX:
					num_ways += 1

			if minX == 1:
				num_ways = 0
				for i in range(n):
					for j in range(n):
						if a[i][j] == "." and (rWinX[i] == 1 or cWinX[j] == 1):
							num_ways += 1

			fout.write(str(num_ways))
		else:
			fout.write("Impossible")

		fout.write("\n")