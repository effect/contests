f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

index = 0
seeds = [int(a) for a in lines[index].split()[1:]]
index += 3
dest = seeds

while index < len(lines):
	source = dest.copy()
	transformers = []
	while index < len(lines) and lines[index].strip() != '':
		line = lines[index]
		d, s, num = (int(a) for a in line.split())
		transformers.append( (d, s, num) )
		index += 1
	index += 2
	# print(transformers)

	dest = [-1] * len(source)
	for i in range(len(source)):
		for tr in transformers:
			if dest[i] != -1:
				continue  # already transformed
			d, s, num = tr
			cur_source = source[i]
			if s <= cur_source < s + num:
				step = cur_source - s
				dest[i] = d + step
	for i in range(len(dest)):
		if dest[i] == -1:
			dest[i] = source[i]
	print(dest)

print(min(dest))