f = open("test.in")
# f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

for line in lines:
	print(line)
