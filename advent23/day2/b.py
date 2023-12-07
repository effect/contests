# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
result = 0
for line in lines:
	game, content = line.split(":")
	game = int(game.split()[-1])
	min_num = {'red': 0, 'green': 0, 'blue': 0}
	for round in content.split(";"):
		for subset in round.strip().split(","):
			subset = subset.strip()
			num, color = subset.split()
			num = int(num)
			if min_num[color] < num:
				min_num[color] = num
	cur = 1
	for v in min_num.values():
		cur *= v
	print(cur)
	result += cur
print(result)
