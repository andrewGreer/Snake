class Game:
	def __init__(self, *, wall_symbol="#", ceiling_symbol="#", board_size=10, character="@"):
		self.wall_symbol = wall_symbol
		self.ceiling_symbol = ceiling_symbol
		self.character=character
		self.rows = board_size+2
		self.cols = board_size+2
		self.board = [[" " for i in range(self.cols)] for _ in range(self.rows)]
		self.board[0] = self.board[-1] = [self.ceiling_symbol for _ in range(self.cols)]
		for row in range(1, self.rows):
			self.board[row][0] = self.board[row][-1] = self.wall_symbol


		print(len(self.board))
		print(len(self.board[0]))

	def __repr__(self):
		return f"Game {self.rows-2}x{self.cols-2}"

	def display(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				print(self.board[row][col], end="")
			print()

	def play(self):
		# starting position
		curr_row = self.rows//2
		curr_col = self.cols//2
		curr_pos = [curr_row, curr_col]
		prev_pos = curr_pos
		self.board[curr_row][curr_col] = self.character
		curr_dir = "w"



		while not (curr_pos[0] == 0 or curr_pos[0] == self.rows-1) and not (curr_pos[1] == 0 or curr_pos[1] == self.cols-1):
			print(curr_pos)
			self.display()
			prev_pos = tuple(curr_pos)
			curr_dir = input()
			if curr_dir == "w":
				curr_pos[0] -= 1
			elif curr_dir == "d":
				curr_pos[1] += 1
			elif curr_dir == "s":
				curr_pos[0] += 1
			elif curr_dir == "a":
				curr_pos[1] -= 1
			self.board[curr_pos[0]][curr_pos[1]] = self.character
			self.board[prev_pos[0]][prev_pos[1]] = " "

		print("Game Over.")


if __name__ == "__main__":

	# game = Game(board_size=10, wall_symbol="|", ceiling_symbol="-")
	game = Game(board_size=20)

	print(game)
	game.display()
	game.play()