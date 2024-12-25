f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def get_register(index):
	return int(lines[index].split()[-1])

A, B, C = (get_register(i) for i in range(3))
p = [int(x) for x in lines[-1].split()[-1].split(',')]
n = len(p)

def get_bit(a, index, cur_value, current_indicies):
	if index >= len(a):
		return 0
	if index == current_indicies:
		return cur_value % 2
	if index == current_indicies + 1:
		return cur_value // 2 % 2
	if index == current_indicies + 2:
		return cur_value // 4 % 2
	return a[index]

def get_3bits(a, index, cur_value, current_indicies):
	b0 = get_bit(a, index, cur_value, current_indicies)
	b1 = get_bit(a, index + 1, cur_value, current_indicies)
	b2 = get_bit(a, index + 2, cur_value, current_indicies)
	return 4 * b2 + 2 * b1 + b0

def set_3bits(a, index, value):
	# print(f'set value {value} at index {index}..{index+2}')
	a[index] = value % 2
	value //= 2
	a[index + 1] = value % 2
	value //= 2
	a[index + 2] = value % 2

def get_number(a):
	result = 0
	power = 1
	for bit in a:
		result += power * bit
		power *= 2
	return result

def find(a, i):
	if i < 0:
		# print(a)
		print(get_number(a))
		return
	out = p[i]
	start = 1 if i == n - 1 else 0
	for x in range(start, 8):
		y = get_3bits(a, 7 - x + 3 * i, x, 3 * i)
		if x ^ y == out:
			set_3bits(a, 3 * i, x)
			find(a, i - 1)


a = [0] * 3 * n
find(a, n - 1)
