f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def parse(s):
	return [int(x) for x in s.split('-')]

def intersection(s1, s2):
	return [max(s1[0], s2[0]), min(s1[1], s2[1])]

result = 0
for line in lines:
	s1, s2 = line.split(',')
	s1 = parse(s1)
	s2 = parse(s2)
	inters = intersection(s1, s2)
	if s1 == inters or s2 == inters:
		result += 1

print(result)
