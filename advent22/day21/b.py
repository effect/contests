f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

tree = dict()

def add_node(line, tree):
	name, expr = line.split(': ')
	if ' ' in expr:
		a, s, b = expr.split()
		expr = f"({a}){s}({b})"
		tree[name] = (expr, a, b)  
	else:
		tree[name] = int(expr)

def calc(name, tree):
	# print(f"calc({name})")
	value = tree[name]
	if type(value) == int:
		return value
	if type(value) == str:
		return value

	expr, a, b = value
	# print(f"expr = {expr}, a = {a}, b = {b}")
	a_value = calc(a, tree)
	b_value = calc(b, tree)
	result = expr.replace(a, str(a_value)).replace(b, str(b_value))
	try:
		result = eval(result)
	except:
		pass
	return result

for line in lines:
	add_node(line, tree)
tree['humn'] = 'x'


# result = calc('root', tree)  # task a

left_result = calc(tree['root'][1], tree)
right_result = calc(tree['root'][2], tree)

print(left_result)
print(right_result)

from sympy import symbols, solve  # one can use https://live.sympy.org if doesn't have sympy installed
x = symbols('x')
solve(left_result + " - " + right_result)
