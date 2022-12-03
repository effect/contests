f = open("test.in")
f = open("a.in")

mapping = {
	"A": "Rock", 
	"B": "Paper", 
	"C": "Scissors", 
	"X": "win", 
	"Y": "draw", 
	"Z": "lose", 
}

points = {
	"Rock": 1, 
	"Paper": 2, 
	"Scissors": 3, 
	"win": 6,
	"draw": 3, 
	"lose": 0, 
}

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
defeat = {
	"Rock": "Scissors", 
	"Scissors": "Paper", 
	"Paper": "Rock", 
}

# def points_for_shape(line):
# 	s = mapping[line[-1]]
# 	return points[s]

def points_for_shape(shape):
	return points[shape]

def outcome_for_first(line): 
	round_outcome = mapping[line[-1]]
	return points[round_outcome]

def get_second_shape(line):
	first_shape = mapping[line[0]]
	round_outcome = mapping[line[-1]]
	options = set(defeat.keys())
	if round_outcome == "draw":
		return first_shape
	if round_outcome == "win":
		return defeat[first_shape]
	options.remove(first_shape)
	options.remove(defeat[first_shape])
	return options.pop()


lines = f.readlines()

result = 0
for line in lines:
	line = line.strip()
	second_shape = get_second_shape(line)

	result += points_for_shape(second_shape)
	result += (6 - outcome_for_first(line))
print(result)
