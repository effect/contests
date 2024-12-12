import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
result = 0

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

# part 1
for line in lines:
	matches = re.findall(pattern, line)
	for match in matches:
		m = [int(a) for a in match]
		result += m[0] * m[1]
print(result)

# part 2
result = 0
line = "".join(lines)
for match in re.finditer(pattern, line):
	index = match.start()
	do_index = line[:index].rfind("do()")
	dont_index = line[:index].rfind("don't()")
	if do_index >= dont_index:
		result += int(match.group(1)) * int(match.group(2))
print(result)