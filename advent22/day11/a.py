# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()] + [""]

M = len(lines) // 7

items = [[] for _ in range(M)]
operations = [""] * M
test_mod = [""] * M
to_if_true = [""] * M
to_if_false = [""] * M
inspections_cnt = [0] * M

for m in range(M):
	cur_lines = lines[7 * m : 7 * (m + 1)]
	items[m] = [int(x) for x in cur_lines[1].split(": ")[1].split(", ")]
	operations[m] = (cur_lines[2].split(" = "))[1]
	test_mod[m] = int(cur_lines[3].split(" by ")[1])
	to_if_true[m] = int(cur_lines[4].split()[-1])
	to_if_false[m] = int(cur_lines[5].split()[-1])

for round in range(20):
	for m in range(M):
		for item in items[m]:
			inspections_cnt[m] += 1
			old = item
			new = eval(operations[m])
			new //= 3	
			if new % test_mod[m] == 0:
				items[to_if_true[m]].append(new)
			else:
				items[to_if_false[m]].append(new)
		items[m] = []

inspections_cnt.sort()
print(inspections_cnt[-1] * inspections_cnt[-2])
