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


def get_intervals(char):
	starts = [1]
	for transformations in rules.values():
		for t in transformations:
			cond = t[0]
			if cond == 'True':
				continue
			if cond[0] != char:
				continue
			if cond[1] == '<':
				border = int(cond[2:])
			elif cond[1] == '>':
				border = int(cond[2:]) + 1
			else:
				print('Error! Broken condition', cond)
			# add border to sorted list of start of intervals
			for index, start in enumerate(starts):
				if start == border:
					break
				if start > border:
					# insert border to index position
					starts.insert(index, border)
					break
			else:
				starts.append(border)
	starts.append(4001)
	return starts


rules = get_rules()
intervals = {char: get_intervals(char) for char in ('x', 'm', 'a', 's')}
for k, v in intervals.items():
	print(len(v))


result = 0
for xi in range(len(intervals['x']) - 1):
	for mi in range(len(intervals['m']) - 1):
		print(intervals['x'][xi], intervals['m'][mi])
		for ai in range(len(intervals['a']) - 1):
			for si in range(len(intervals['s']) - 1):
				x = intervals['x'][xi]
				m = intervals['m'][mi]
				a = intervals['a'][ai]
				s = intervals['s'][si]
				state = get_final_state()
				if state == 'A':
					result += (intervals['x'][xi + 1] - x) * (intervals['m'][mi + 1] - m) * (intervals['a'][ai + 1] - a) * (intervals['s'][si + 1] - s)
print(result)