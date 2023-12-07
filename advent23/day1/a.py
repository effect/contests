f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

def get_number(s):
	first_digit = None
	last_digit = None
	for c in s:
		if c.isdigit():
			if first_digit is None:
				first_digit = c
			last_digit = c
	return int(first_digit + last_digit) 


res = 0
for line in lines:
	cur = get_number(line)
	res += cur

print(res)
