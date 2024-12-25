
def get_number(x):
	number = 0
	for var in variables:
		if var[0] == x: 
			value = variables[var]
			ind = int(var[1:])
			number += (1 << ind) * value
	return number

def correct_z(Z):
	z = []
	while Z > 0:
		z.append(Z % 2)
		Z >>= 1
	return z


X = get_number('x')
Y = get_number('y')
print(X, Y)
Z = X + Y
print(Z)
z = correct_z(Z)
print(z ,len(z))


result = 0
for var in expressions:
	if var[0] == 'z':
		zb = calc(var)
		ind = int(var[1:])
		result += (1 << ind) * zb
print(result)

potentially_wrong = Counter()

def mark_path(node):
	if node[0] in ('x', 'y'):
		return 
	potentially_wrong[node] += 1
	(a, op, b) = expressions[node]
	mark_path(a)
	mark_path(b)

for var in expressions:
	if var[0] == 'z':
		ind = int(var[1:])
		if variables[var] != z[ind]:
			print(ind)
			mark_path(var)
print(potentially_wrong)
print(len(potentially_wrong))
