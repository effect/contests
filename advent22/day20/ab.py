f = open("test.in")
f = open("input.txt")

MULT = 1  # task a
MULT = 811589153  # task b

ITERATIONS = 1  # task a
ITERATIONS = 10  # task b

lines = [line.strip() for line in f.readlines()]
a = [int(x) for x in lines]
n = len(a)

# print(min(a), max(a))

a = [(i, x * MULT) for i, x in enumerate(a)]

def get_current_index(a, index):
	# print(a, index)
	for i, item in enumerate(a):
		if type(item) == int:
			continue
		if item[0] == index:
			return i

a_initial = a.copy()
for iterations in range(ITERATIONS):  
	for i, x in a_initial:
		current_index = get_current_index(a, i)

		a.remove((i, x))
		steps_right = x % (n - 1)
		if current_index + steps_right <= n - 1:
			a.insert(current_index + steps_right, (i, x))
		else:
			a.insert(current_index + steps_right - n + 1, (i, x))

print(a) 

result = 0
index_0 = [pair[1] for pair in a].index(0)
for i in range(3):
	index = (index_0 + (i + 1) * 1000) % n
	result += a[index][1]

print(result)