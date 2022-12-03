# with open("test.in") as f:
with open("a1.in") as f:
	lines = f.readlines() + [""]
	a = []
	cur_sum = 0
	for line in lines:
		if line.strip() == "":
			a.append(cur_sum)
			cur_sum = 0
		else:
			cur_sum += int(line.strip())
	
	a = sorted(a)
	print(a)
	print(a[-1] + a[-2] + a[-3])

