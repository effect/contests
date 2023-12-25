f = open("test.in")
f = open("input.txt")

a = [line.strip() for line in f.readlines()]
# f = open("test.out", "w")
f = open("output.txt", "w")
for i, line in enumerate(a):
	line = line.replace('#', ' ')
	line = line.replace('.', 'o')
	line = line.replace('>', 'o')  # task B
	line = line.replace('v', 'o')  # task B
	f.write(line + '\n')
