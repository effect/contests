from collections import Counter, defaultdict

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]


def init():
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
	return variables, expressions


def var_name(xyz, index):
	return xyz + str(index).zfill(2)


def get_with_operator(exp1, exp2, operator):
	try:
		a, op, b = expressions[exp2]
		if op == operator:
			return exp2
	except:
		pass
	try:
		a, op, b = expressions[exp1]
		if op == operator:
			return exp1
	except:
		pass



NB = 46
rev = [0] * NB
forw = [0] * NB
variables, expressions = init() 

to_swap = [
('pfw', 'z39'), 
('shh', 'z21'), 
('dqr', 'z33'), 
('vgs', 'dtk')
]

for a, b in to_swap:
	expressions[a], expressions[b] = expressions[b], expressions[a]

for ind in range(1, NB):
	z = var_name('z', ind)
	(exp1, xor, exp2) = expressions[z]
	if xor != "XOR":
		print(ind, z, ' = ', expressions[z])
		continue
	a_xor_b = get_with_operator(exp1, exp2, 'XOR')
	if a_xor_b is None:
		print(ind, z, ' = ', expressions[z], "no XOR: ", exp1, ' = ', expressions[exp1], exp2, ' = ', expressions[exp2])
	else:
		a, xor, b = expressions[a_xor_b]
		if set([a, xor, b]) != set([var_name('x', ind), 'XOR', var_name('y', ind)]):
			print(ind, z, ' = ', expressions[z], expressions[exp1], expressions[exp2])

	x_or_y = get_with_operator(exp1, exp2, 'OR')
	if x_or_y is None:
		print(ind, z, ' = ', expressions[z], "no OR: ", exp1, ' = ', expressions.get(exp1), exp2, ' = ', expressions.get(exp2))
	else:
		x, op_or, y = expressions[x_or_y]
		try:
			ex1, opx, ex2 = expressions[x]
			ey1, opy, ey2 = expressions[y]
			if opx != 'AND' or opy != 'AND':
				print("no 2 AND", ind, z, ' = ', expressions[z], x_or_y, ' = ', x, op_or, y, x, ' = ', ex1, opx, ex2, y, ' = ', ey1, opy, ey2)
		except:
				print("Excpetion", ind, z, ' = ', expressions[z], x_or_y, ' = ', x, op_or, y, x, ' = ', expressions.get(x), y, ' = ', expressions.get(y))


result = []
for a, b in to_swap:
	result.append(a)
	result.append(b)
result = sorted(result)
print(','.join(result))
