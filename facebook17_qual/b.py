import math

with open("b.in") as fin, open("b.out", "w") as fout:
	T = int(fin.readline())
	for t in range(T):
		fout.write("Case #" + str(t + 1) + ": ")
		
		n = int(fin.readline())
		w = [0] * n
		for i in range(n):
			w[i] = int(fin.readline())
		w.sort(reverse=True)
		res = 0
		W = 50

		i = 0
		j = n - 1
		while i <= j:
			top = w[i]
			num = W / top
			if W % top > 0:
				num += 1
			num -= 1
			j -= num

			if i <= j:
				res += 1
			i += 1
		
		fout.write(str(res))
		fout.write("\n")