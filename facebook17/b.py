with open("b.in") as fin, open("b.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")
		
		n, r = (int(x) for x in fin.readline().split())
		
		x = [0] * n
		y = [0] * n
		for i in range(n):
			x[i], y[i] = (int(x) for x in fin.readline().split())

		res = 0
		for ix in range(n):
			for iy in range(n):
				if x[iy] < x[ix] or x[iy] > x[ix] + r:
					continue
				if y[ix] < y[ix] or y[ix] > y[iy] + r:
					continue
				X1 = x[ix]
				Y1 = y[iy]

				for jx in range(n):
					for jy in range(n):
						if x[jy] < x[jx] or x[jy] > x[jx] + r:
							continue
						if y[jx] < y[jx] or y[jx] > y[jy] + r:
							continue
						X2 = x[jx]
						Y2 = y[jy]

						cnt = 0
						for i in range(n):
							if ((X1 <= x[i] <= X1 + r) and (Y1 <= y[i] <= Y1 + r)) or ((X2 <= x[i] <= X2 + r) and (Y2 <= y[i] <= Y2 + r)):
								cnt += 1
						res = max(res, cnt)

		fout.write(str(res))
		fout.write("\n")