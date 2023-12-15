f = open("test.in")
f = open("input.txt")

a = [list(line.strip()) for line in f.readlines()]
nrow = len(a)
ncol = len(a[0])
print(nrow, ncol)
for col in range(ncol):
	for row in range(nrow):
		if a[row][col] == 'O':
			# bubble up
			i = row
			while i - 1 >= 0 and a[i - 1][col] == '.':
				a[i - 1][col] = 'O'
				a[i][col] = '.'
				i -= 1
# for line in a:
# 	print(''.join(line))
result = 0
for col in range(ncol):
	for row in range(nrow):
		if a[row][col] == 'O':
			result += nrow - row
print(result)
