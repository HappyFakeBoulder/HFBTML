import time
class Error_Error(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)
class ProgramCardLine():
	def __init__(self, write, move, nextCard):
		if type(write) != str or (type(move) != int or type(nextCard) != int):
			raise TypeError("Invalid argument(s) for __init__ of ProgramCardLine")
		self.write = write
		self.move = move
		self.nextCard = nextCard
class ProgramCard():
	def __init__(self, data):
		if type(data) != dict:
			raise TypeError("Invalid argument for __init__ of ProgramCard")
		self.data = data
class TuringMachine():
	def __init__(self, cards):
		if type(cards) != list:
			raise TypeError("Invalid argument for __init__ of TuringMachine")
		self.cards = cards
	def run(self, startingTape, startingCard):
		if type(startingTape) != list or type(startingCard) != int:
			raise TypeError("Invalid argument(s) for run of TuringMachine")
		self.tape = [" "] * 1024 + startingTape + [" "] * 1024
		self.currentCard = startingCard
		self.headPos = 1024
		while True:
			time.sleep(0.1)
			try:
				self.doHere = self.cards[self.currentCard].data[self.tape[self.headPos]]
			except IndexError:
				raise Error_Error("WHAT ARE YOU DOING?!")
			except KeyError:
				pass
			try:
				self.tape[self.headPos] = self.doHere.write
				self.headPos += self.doHere.move
				self.currentCard = self.doHere.nextCard
			except:
				raise Error_Error("WHAT ARE YOU DOING?!")
			print("\n" * 50 + " " * 20 + str(self.currentCard) + "\n" + " " * 20 + "|" + "\n" + " " * 20 + "v" + "\n" + "".join(self.tape[self.headPos - 20:self.headPos + 20]))
