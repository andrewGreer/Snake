class Game:
	def __init__(self, *, wall_symbol="#", ceiling_symbol="#", board_size=10):
		self.wall_symbol = wall_symbol
		self.ceiling_symbol = ceiling_symbol
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

	def play():
		pass


if __name__ == "__main__":

	# game = Game(board_size=10, wall_symbol="|", ceiling_symbol="-")
	game = Game()

	print(game)
	print(game.display())