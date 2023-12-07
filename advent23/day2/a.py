# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

f = open("test.in")
f = open("input.txt")

NUM = {'red': 12, 'green': 13, 'blue': 14}


lines = [line.strip() for line in f.readlines()]
result = 0
for line in lines:
	game, content = line.split(":")
	game = int(game.split()[-1])
	is_game_ok = True
	for round in content.split(";"):
		for subset in round.strip().split(","):
			subset = subset.strip()
			num, color = subset.split()
			num = int(num)
			if num > NUM[color]:
				is_game_ok = False
	if is_game_ok:
		print(game)
		result += game
print(result)
