# f = open("test.in")
f = open("input.txt")
lines = [line.strip() for line in f.readlines()]

f = open("input.graph", "w")
for line in lines:
	l, r = line.split(": ")
	r = "{" + r + "}"
	line = l + " -- " + r
	f.write(line + "\n")
