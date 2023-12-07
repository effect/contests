f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]


def in_bounds(i, j):
	return i >= 0 and i < len(lines) and j >= 0 and j < len(lines[i])


def get_numbers_around(i, j):
	numbers_positions = set()
	for di in range(-1, 2):
		for dj in range(-1, 2):
			ii = i + di
			jj = j + dj
			if in_bounds(ii, jj) and lines[ii][jj].isdigit():
				number_start = jj
				number_end = jj
				while number_start >= 0 and lines[ii][number_start].isdigit():
					number_start -= 1
				number_start += 1
				while number_end < len(lines[ii]) and lines[ii][number_end].isdigit():
					number_end += 1
				numbers_positions.add((ii, number_start, number_end))
	numbers = []
	for positions in numbers_positions:
		ii, number_start, number_end = positions
		numbers.append(int(lines[ii][number_start:number_end]))
	return numbers


result = 0
for i, line in enumerate(lines):
	for j in range(len(line)):
		if line[j] == '*':
			numbers = get_numbers_around(i, j)
			if len(numbers) >= 2:
				print(numbers)
				result += numbers[0] * numbers[1]
print(result)