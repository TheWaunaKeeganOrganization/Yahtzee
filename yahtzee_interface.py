import itertools, random
from yahtzee_categories import *
class Player:
	def __init__(self):
		self.scorecard = {}
		self.hand = []
		self.table = [1,1,1,1,1]
		self.scorecard['ones'] = None
		self.scorecard['twos'] = None
		self.scorecard['threes'] = None
		self.scorecard['fours'] = None
		self.scorecard['fives'] = None
		self.scorecard['sixes'] = None
		self.scorecard['threeOfAKind'] = None
		self.scorecard['fourOfAKind'] = None
		self.scorecard['smallStraight'] = None
		self.scorecard['largeStraight'] = None
		self.scorecard['fullHouse'] = None
		self.scorecard['chance'] = None
		self.scorecard['yahtzee'] = None

	def roll(self):
		self.table = list(random.choice(list(itertools.product(range(1,7),repeat = len(self.table)))))

	def keep(self, keepers):
		for n in keepers:
			self.table.remove(n)
			self.hand.append(n)

	def assign(self,assignment):
		try:
			if assignment != None:
				scorecard[assignment] = eval(assignment)(self.table + self.hand)
			else:
				raise 
		except:
			print 'point assignment is not valid'
			p = raw_input('choose a category to assign your points to')
			assign(self,p)

	def move(self):
		raw_input('roll? y/n')


player1 = Player()
player2 = Player()
