f = open("test.in")
f = open("input.txt")

line = "".join([line.strip() for line in f.readlines()])

n = len(line)
a = [[] for _ in range(n)]
for i in range(n):
	value = -1 if i % 2 else i // 2
	a[i] = [value for _ in range(int(line[i]))]

# print(a)

j = len(a) - 1
while j >= 0:
	while (len(a[j]) == 0) or (a[j][0] == -1):
		j -= 1

	i = 0
	while i < j:
		if (len(a[i]) >= len(a[j])) and (a[i][0] == -1):
			break
		i += 1

	if i < j:
		# moving
		new_empty_len = len(a[i]) - len(a[j])
		a[i] = a[j]
		a[j] = [-1] * len(a[j])
		a.insert(i + 1, [-1] * new_empty_len)
	else:
		j -= 1

# print(a)
a = [item for sublist in a for item in sublist]
# print(a)

result = 0
for index, value in enumerate(a):
  if value >= 0:
  	result += index * value
print(result)