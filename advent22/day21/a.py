f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

tree = dict()

def add_node(line, tree):
	name, expr = line.split(': ')
	if ' ' in expr:
		a, s, b = expr.split()
		tree[name] = (expr, a, b)  # print(f"calc({name})")
	else:
		tree[name] = int(expr)

def calc(name, tree):
	# print(f"calc({name})")
	value = tree[name]
	if type(value) == int:
		return value
	expr, a, b = value
	# print(f"expr = {expr}, a = {a}, b = {b}")
	a_value = calc(a, tree)
	b_value = calc(b, tree)
	result = eval(expr.replace(a, str(a_value)).replace(b, str(b_value)))
	return result

for line in lines:
	add_node(line, tree)

result = calc('root', tree)
print(int(result))