from collections import Counter
f = open("test.in")
f = open("input.txt")

def options(mask, index=0):
	if index >= len(mask):
		return [mask]
	if mask[index] == '.' or mask[index] == '#':
		return options(mask, index + 1)
	if mask[index] == '?':
		return options(mask[:index] + "." + mask[index + 1:], index + 1) + options(mask[:index] + "#" + mask[index + 1:], index + 1)
	return []


def satisfy(a, cnts):
	parts = a.split('.')
	parts = [p for p in parts if p]
	if len(parts) != len(cnts):
		return False
	for i in range(len(parts)):
		if len(parts[i]) != cnts[i]:
			return False
	return True


lines = [line.strip() for line in f.readlines()]
result = 0
# counter = Counter()
for line in lines:
	mask, cnts = line.strip().split()
	cnts = [int(a) for a in cnts.split(',')]
	print(mask, cnts)
# 	counter[mask.count('?')] += 1
# print(counter)
	num = 0
	for a in options(mask):
		if satisfy(a, cnts):
			num += 1
	print(num)
	result += num
print(result)