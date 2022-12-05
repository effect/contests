f = open("test.in")
f = open("input.txt")

lines = [line.strip("\n") for line in f.readlines()]

split_index = lines.index("")
n = split_index - 1
ncols = int(lines[n].split()[-1])

commands = lines[split_index + 1:]
lines = [line + " " * (4 * ncols - len(line)) for line in lines[:n]]

# print(lines)
# print(commands)

def gen_col(i):
	index = 4 * i + 1
	a = [" "] * n
	for i in range(n):
		a[i] = lines[i][index]
	return "".join(a)

cols = [gen_col(i).strip() for i in range(ncols)]
print(cols)

for cmd in commands:
 	parts = cmd.split()
 	num, ind_from, ind_to = (int(x) for x in parts[1::2])
 	ind_from -= 1
 	ind_to -= 1

 	sub = cols[ind_from][:num]
 	cols[ind_to] = sub + cols[ind_to]
 	cols[ind_from] = cols[ind_from][len(sub):]

print(cols)
result = [cols[i][0] for i in range(ncols)]
print("".join(result))