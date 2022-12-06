# f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

N = 14  # 4 for a
for line in lines:
	for index in range(N - 1, len(line) + 1):
		s = set(line[index - N + 1 : index + 1])
		if len(s) == N:
			print(index + 1)
			break
