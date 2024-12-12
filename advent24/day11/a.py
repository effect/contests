f = open("test.in")
f = open("input.txt")

line = [line.strip() for line in f.readlines()][0]
a = [int(x) for x in line.split()]
NUM = 25  # part 1
# NUM = 75  # part 2 -- too slow => b.py

def blink(a):
	b = []
	for x in a:
		if x == 0:
			b.append(1)
		else:
			strx = str(x)
			if len(strx) % 2 == 0:
				x1 = strx[:len(strx) // 2]
				x2 = strx[len(strx) // 2 : ]
				b.append(int(x1))
				b.append(int(x2))
			else:
				b.append(x * 2024)
	return b

for i in range(NUM):
	a = blink(a)

print(len(a))