f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

variables = dict()
expressions = dict()

for line in lines:
	if ':' in line:
		var, value = (part.strip() for part in line.split(':'))
		variables[var] = int(value)
	elif '->' in line:
		expr, res = (part.strip() for part in line.split('->'))
		a, op, b = expr.split()
		expressions[res] = (a, op, b)

# print(variables)
# print(expressions)


def calc(var):
	if var in variables:
		return variables[var]
	(a, op, b) = expressions[var]
	av = calc(a)
	bv = calc(b)
	if op == 'AND':
		result = av and bv
	if op == 'OR':
		result = av or bv
	if op == 'XOR':
		result = av ^ bv
	variables[var] = result
	return result


result = 0
for var in expressions:
	if var[0] == 'z':
		z = calc(var)
		ind = int(var[1:])
		# print(ind, z)
		result += (1 << ind) * z
print(result)

