f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]


def get_condition(transformation):
	if ':' in transformation:
		return transformation[:transformation.index(':')]
	else:
		return 'True'


def get_destination(transformation):
	if ':' in transformation:
		return transformation[transformation.index(':') + 1:]
	else:
		return transformation


def get_rules():
	rules = {}
	for line in lines:
		if line == "":
			return rules
		name, transformations = line[:line.index('{')], line[line.index('{') + 1: -1]
		transformations = transformations.split(',')
		transformations = [(get_condition(part), get_destination(part)) for part in transformations]
		rules[name] = transformations


def get_final_state():
	state = 'in'
	while 1:
		state_rules = rules[state]
		for rule in state_rules:
			if eval(rule[0]):
				state = rule[1]
				if state in ['A', 'R']:
					return state
				break


rules = get_rules()
result = 0
for line in lines:
	if line.startswith("{"):
		pairs = line[1:-1].split(',')
		cur_sum = 0
		for pair in pairs:
			key, value = pair.split('=')
			exec(f"{key} = {value}")
			cur_sum += int(value)

		state = get_final_state()
		if state == 'A':
			result += cur_sum
print(result)