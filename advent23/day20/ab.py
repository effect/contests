from queue import Queue
from collections import defaultdict
import math

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

FLIP = '%'
CONJ = '&'
BROADCAST = 'broadcaster'
ITERATIONS = 1000

LOW = 0
HIGH = 1

# types of item in the queue
NODE = 0      
ACTION = 1

states = {} # node name -> LOW/HIGH
types = {}  # node name -> type of node (flip-flop, conjunction etc)
out = {}    # node name -> [node names] (outbound edges)
inb = defaultdict(list)    # node name -> [node names] (inbound edges)

for line in lines:
	fr, to = line.split(' -> ')
	to = to.split(', ')
	for t in (FLIP, CONJ, BROADCAST):
		if fr.startswith(t):
			fr = fr[len(t):]
			types[fr] = t			
			break
	states[fr] = LOW
	out[fr] = to
	for t in to:
		inb[t].append(fr)
		if t not in types:
			types[t] = ''

# print(out)
# print(inb)
# print(states)
# print(types)


WANT_NODES = ['qs', 'sv', 'pg', 'sp']
def check_task_b(node, iteration):
	# return  # for task A
	if node in WANT_NODES:
		print(f'{node} visited on iteration ', iteration + 1)


num_low = 0
num_high = 0

# for iteration in range(ITERATIONS):  # task A
for iteration in range(ITERATIONS * 20):  # task B
	q = Queue()
	cur_high = 0
	cur_low = 1  # account for button -low-> broadcaster
	q.put((NODE, ''))
	while not q.empty():
		t, node = q.get()
		# print(t, node, cur_low, cur_high)
		if t == NODE:
			if node == '':  # broadcaster
				cur_low += len(out[node])
				for next_node in out[node]:
					q.put((NODE, next_node))
					check_task_b(next_node, iteration)
			elif types[node] == FLIP:
				# FLIP node reacts only on LOW signals
				next_state = 1 - states[node]
				q.put((ACTION, node))
				if next_state == HIGH:
					cur_high += len(out[node])
					for next_node in out[node]:
						# send HIGH signal only to CONJ nodes
						if types[next_node] == CONJ:
							q.put((NODE, next_node))
				else:  # next_state == LOW
					cur_low += len(out[node])
					for next_node in out[node]:
						q.put((NODE, next_node))
						check_task_b(next_node, iteration)
			elif types[node] == CONJ:
				incoming_signals = [states[v] for v in inb[node]]
				out_signal = 1 - all(incoming_signals)
				# print(incoming_signals, all(incoming_signals), out_signal)
				states[node] = out_signal
				if out_signal == LOW:
					cur_low += len(out[node])
				else:
					cur_high += len(out[node])
				for next_node in out[node]:
					if types[next_node] == FLIP and out_signal == HIGH:
						continue
					q.put((NODE, next_node))
					if out_signal == LOW:
						check_task_b(next_node, iteration)
		elif t == ACTION:
			states[node] = 1 - states[node]

	# print(cur_low, cur_high)
	# print(states)
	num_low += cur_low
	num_high += cur_high

# task A
print(num_low, num_high)
print(num_low * num_high)

# task B
# pg visited on iteration  3761
# sp visited on iteration  3907
# sv visited on iteration  3919
# qs visited on iteration  4051
print(math.lcm(3761, 3907, 3919, 4051))