import copy
f = open("test.in")
f = open("input.txt")

a = [list(line.strip()) for line in f.readlines()]
nrow = len(a)
ncol = len(a[0])
print(nrow, ncol)

def bubble_up():
	for col in range(ncol):
		for row in range(nrow):
			if a[row][col] == 'O':
				# bubble up
				i = row
				while i - 1 >= 0 and a[i - 1][col] == '.':
					a[i - 1][col] = 'O'
					a[i][col] = '.'
					i -= 1


def rotate():
	global a 
	b = copy.deepcopy(a)
	for i in range(nrow):
		for j in range(ncol):
			b[i][j] = a[nrow - 1 - j][i]
	a = copy.deepcopy(b)


def tilt_all():
	for i in range(4): 
		bubble_up()
		rotate()


def table_to_str(a):
	return "".join([''.join(line) for line in a])


history = {}
history[table_to_str(a)] = 0
num_iterations = 1000000000
for it in range(1, num_iterations):
	tilt_all()
	s = table_to_str(a)
	if s in history:
		print("First occurence: ", history[s])
		print("Second occurence: ", it)
		break
	history[s] = it

cycle = it - history[s]
num_iterations -= history[s]
num_iterations %= cycle
for it in range(num_iterations):
	tilt_all()


result = 0
for col in range(ncol):
	for row in range(nrow):
		if a[row][col] == 'O':
			result += nrow - row
print(result)