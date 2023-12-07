f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def is_symbol(i, j):
	if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[i]):
		if lines[i][j] != '.' and not lines[i][j].isdigit():
			return True
	return False


def has_symbol_around(row_index, start, end):
	for i in range(row_index - 1, row_index + 2):
		for j in range(start - 1, end + 1):
			if is_symbol(i, j):
				return True
	return False


result = 0
for row_index, line in enumerate(lines):
	number_start = 0
	while number_start < len(line):
		# to find start of number
		while number_start < len(line) and not line[number_start].isdigit():
			number_start += 1
		if number_start >= len(line):
			break

		# to find end of number
		number_end = number_start
		while number_end < len(line) and line[number_end].isdigit():
			number_end += 1

		# (row_index, [number_start .. number_end)) is a number
		if has_symbol_around(row_index, number_start, number_end):
			cur = int(line[number_start:number_end])
			print(cur)
			result += cur

		number_start = number_end

print(result)