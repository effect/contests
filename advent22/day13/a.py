f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()] + [""]
N = len(lines) // 3
total = 0


def compare_values(left, right):
	if type(left) == int and type(right) == int:
		return left - right
	if type(left) == int:
		return compare_lists([left], right)
	if type(right) == int:
		return compare_lists(left, [right])
	return compare_lists(left, right)

def compare_lists(left, right):
	for index in range(max(len(left), len(right))):
		if index >= len(left):
			return -1
		if index >= len(right):
			return 1

		left_value = left[index]
		right_value = right[index]
		result = compare_values(left_value, right_value)
		if result != 0:
			return result
	return 0


for pair_index in range(N):
	left = eval(lines[3 * pair_index])
	right = eval(lines[3 * pair_index + 1])

	result = compare_lists(left, right)
	if result < 0:
		total += pair_index + 1
		print(pair_index + 1)

print(total)