import math

with open("a.in") as fin, open("a.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		p, x, y = (int(s) for s in fin.readline().split())
		fout.write("Case #" + str(t + 1) + ": ")
		
		R = 50
		x -= R
		y -= R
		an = 2 * math.pi * p / 100.
		r2 = x * x + y * y

		res = "white"
		if p > 0 and r2 <= R * R:
			phi = math.atan2(y, x)
			nph = -phi + math.pi / 2
			if nph < -1e-6:
				nph += 2 * math.pi
			if nph <= an:
				res = "black"

		fout.write(res)
		fout.write("\n")