f = open("test.in")
f = open("input.txt")

def calc(field):
	result = 0
	nrows = len(field)
	ncols = len(field[0])

	# build similarity matrices for all columns and rows
	col_eq = [[True] * ncols for _ in range(ncols)]
	for i in range(ncols):
		for j in range(ncols):
			for k in range(nrows):
				if field[k][i] != field[k][j]:
					col_eq[i][j] = False
					break
	
	row_eq = [[True] * nrows for _ in range(nrows)]
	for i in range(nrows):
		for j in range(nrows):
			for k in range(ncols):
				if field[i][k] != field[j][k]:
					row_eq[i][j] = False
					break

	# test each column as a potential symmetry line
	for test_col in range(ncols - 1):
		# test line between test_col and (test_col+1)	
		symmetry = True
		left = test_col
		right = test_col + 1
		while 1:
			if left < 0:
				break
			if right >= ncols:
				break
			if not col_eq[left][right]:
				symmetry = False
				break
			left -= 1
			right += 1
		if symmetry:
			result += test_col + 1

	# now test each row similarly
	for test_row in range(nrows - 1):
		symmetry = True
		up = test_row
		down = test_row + 1
		while 1:
			if up < 0:
				break
			if down >= nrows:
				break
			if not row_eq[up][down]:
				symmetry = False
				break
			up -= 1
			down += 1
		if symmetry:
			result += (test_row + 1) * 100

	return result

lines = [line.strip() for line in f.readlines()] + [""]
result = 0
field = []
for line in lines:
	if line.strip() == "":
		result += calc(field)
		field = []
	else:
		field.append(line)
print(result)