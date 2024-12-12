f = open("test.in")
f = open("input.txt")

line = "".join([line.strip() for line in f.readlines()])
n = len(line)
a = [[] for _ in range(n)]
for i in range(n):
	value = -1 if i % 2 else i // 2
	a[i] = [value for _ in range(int(line[i]))]
# print(a)
a = [item for sublist in a for item in sublist]
# print(a)

i = 0
j = len(a) - 1
while i < j:
	if a[i] >= 0:
		i += 1
		continue
	if a[j] < 0:
		j -= 1
		continue
	a[i], a[j] = a[j], a[i]
	i += 1
	j -= 1
# print(a)

result = 0
for index, value in enumerate(a):
  if value >= 0:
  	result += index * value
print(result)