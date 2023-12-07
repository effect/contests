f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

index = {str(i) : i for i in range(10)}
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words = {words[i] : i + 1 for i in range(9)}
index.update(words)

def get_number(s):
	left_index = len(s)
	right_index = -1
	first = None
	last = None
	for k, v in index.items():
		li = s.find(k)
		ri = s.rfind(k)
		if li >= 0 and li < left_index:
			left_index = li
			first = v
		if ri > right_index:
			right_index = ri
			last = v
	return 10 * first + last


res = 0
for line in lines:
	cur = get_number(line)
	print(cur)
	res += cur

print(res)