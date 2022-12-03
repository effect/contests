with open("a1.in") as f:
	lines = f.readlines() + [""]
	max_sum = 0
	cur_sum = 0
	for line in lines:
		if line.strip() == "":
			max_sum = max(max_sum, cur_sum)
			cur_sum = 0
		else:
			cur_sum += int(line.strip())
	print(max_sum)

