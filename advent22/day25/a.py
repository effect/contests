f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

DIGITS_5DS = ['0', '1', '2', '=', '-']

def symbol_to_value(c: str) -> int:
	if '0' <= c <= '2':
		return int(c)
	if c == '-':
		return -1
	if c == '=':
		return -2 

def from_5ds(number: str) -> int:
	result = 0
	p = 1
	for c in reversed(number):
		a = symbol_to_value(c)
		result += a * p
		p *= 5
	return result

def to_5ds(number: int) -> str:
	result = []
	while number > 0:
		last = number % 5
		symb = DIGITS_5DS[last]
		result.append(symb)
		
		number -= symbol_to_value(symb)
		number //= 5
	return "".join(reversed(result))

a = [from_5ds(i) for i in lines]
print(a)
s = sum(a)
print(s)
print(to_5ds(s))