from queue import Queue

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
END = 4001


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


def get_number(intervals):
	result = 1
	for a in intervals.values():
		result *= a[1] - a[0]
	return result


rules = get_rules()

result = 0
q = Queue()
q.put(('in', {char: (1, END) for char in ('x', 'm', 'a', 's')}))
while not q.empty():
	name, intervals = q.get()
	if name == 'R':
		continue
	if name == 'A':
		result += get_number(intervals)
		continue
	transformations = rules[name]

	for t in transformations:
		cond, next_state = t
		if cond == 'True':
			q.put((next_state, intervals.copy()))
			break
		char = cond[0]
		q_interval = intervals[char]
		if cond[1] == '<':
			border = int(cond[2:])
			if border <= q_interval[0]:
				continue
			if border < q_interval[1]:
				next_intervals = intervals.copy()
				next_intervals[char] = (q_interval[0], border)
				q.put((next_state, next_intervals))
				# adjust intervals to reflect that current condition wasn't satisfied (as we will iterate to the next transformation)
				intervals[char] = (border, q_interval[1])
			else:  # border >= q_interval[1] => cond is True
				q.put((next_state, intervals.copy()))
				break
		elif cond[1] == '>':
			border = int(cond[2:]) + 1
			# condition: value(char) >= border
			if border <= q_interval[0]:  # cond is True
				q.put((next_state, intervals.copy()))
				break
			if border < q_interval[1]:
				next_intervals = intervals.copy()
				next_intervals[char] = (border, q_interval[1])
				q.put((next_state, next_intervals))
				# adjust intervals to reflect that current condition wasn't satisfied (as we will iterate to the next transformation)
				intervals[char] = (q_interval[0], border)
			else:  # border >= q_interval[1] => cond is False
				continue
		else:
			print('Error! Broken condition', cond)

print(result)