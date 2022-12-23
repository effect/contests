f = open("test.in")
f = open("input.txt")

NUM_ITERATIONS = 2022

command = [line.strip() for line in f.readlines()][0]
n = len(command)

class Rock:
	'''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
	'''

	def __init__(self, number):
		number %= 5  # numbers start with 0
		if number == 0:
			self.pieces = [ [3, 0], [4, 0], [5, 0], [6, 0] ]
		elif number == 1:
			self.pieces = [ [3, 1], [4, 0], [4, 1], [4, 2], [5, 1] ]
		elif number == 2:
			self.pieces = [ [3, 0], [4, 0], [5, 0], [5, 1], [5, 2] ]
		elif number == 3:
			self.pieces = [ [3, 0], [3, 1], [3, 2], [3, 3] ]
		elif number == 4:
			self.pieces = [ [3, 0], [3, 1], [4, 0], [4, 1] ]

	def move_horizontal(self, iteration, direction=1):
		iteration %= n
		dx = -direction if command[iteration] == '<' else direction
		for piece in self.pieces:
			piece[0] += dx
		# print(f"move horizontal: {self}")

	def move_vertical(self, direction=1):
		for piece in self.pieces:
			piece[1] -= direction
		# print(f"move vertical: {self}")


	def init_vertical(self, y):
		for piece in self.pieces:
			piece[1] += y

	def __str__(self):
		return " ".join(f"({piece[0]} {piece[1]})" for piece in self.pieces)


def is_intersects(rock):
	for piece in rock.pieces:
		x, y = piece
		if x <= 0 or x > 7:
			return True
		if y <= 0:
			return True
		if y < len(rows):
			if rows[y][x] > 0:
				return True
	return False


def update_field(rock):
	for piece in rock.pieces:
		x, y = piece
		while y >= len(rows):
			rows.append([0] * 8)	
		rows[y][x] = 1


def show_field():
	print()
	for row in rows[::-1]:
		print("".join(['#' if c else '.' for c in row[1:]]))


def simulate(rock, steps):
	while True:
		rock.move_horizontal(steps)
		if is_intersects(rock):
			rock.move_horizontal(steps, -1)
		steps += 1
		rock.move_vertical()
		if is_intersects(rock):
			rock.move_vertical(-1)
			break
	update_field(rock)
	return steps


rows = [ [] ]  # row 0 imitates floor
steps = 0
prev_height = 1
for iteration in range(NUM_ITERATIONS):
	# show_field()
	rock = Rock(iteration)
	y = len(rows) + 3
	rock.init_vertical(y)
	steps = simulate(rock, steps)

print(len(rows) - 1)