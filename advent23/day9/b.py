f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
	a = [[int(x) for x in line.strip().split()]]
	n = len(a[0])
	row = 0
	while 1:
		if all(x == a[row][0] for x in a[row]):
			break
		row += 1
		# start to build a row 
		a.append([])
		for i in range(n - row):
			a[row].append(a[row - 1][i + 1] - a[row - 1][i])
		# print(a)

	# now go back
	while row > 0:
		a[row - 1].insert(0, a[row - 1][0] - a[row][0])
		# print(a[row - 1])
		row -= 1
	# print(a[0][0])
	result += a[0][0]
print(result)