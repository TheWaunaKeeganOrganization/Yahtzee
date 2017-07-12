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
import itertools, random, sys
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

	def assign(self):
		print self.scorecard
		assignment = raw_input('To which category do you wish to assign them (see the above scorecard):')
		try:
			if assignment != None:
				scorecard[assignment] = eval(assignment)(self.table + self.hand)
			else:
				raise 'myerror'
		except:
			print 'point assignment is not valid'
			p = raw_input('choose a category to assign your points to:')
			assign(self,p)

	def keeps(self):
		 k = raw_input('which dice do you want to keep (ex. for a roll of [5,4,3,4,6], you could write 4,4): \n').split(',')
		 tab = copy.deepcopy(self.table)
		 for n in k:
		 	if n in tab:
		 		tab.remove(n)
		 	else:
		 		print 'that is not a valid input'
		 		return keeps(self)
		 return k


	def move(self):
		yn = raw_input('input anything to roll')
		if yn:
			roll()
		print self.table
		assignyn = raw_input('Do you want to assign your points to a category? y/n:')
		if assignyn == 'y' or assignyn == 'Y':
			assign()
			return None
		keeping = keeps()
		keep(keeping)
		yn = raw_input('input anything to roll')
		if yn:
			roll()
		self.table += self.hand
		self.hand = []
		print self.table
		assignyn = raw_input('Do you want to assign your points to a category? y/n:')
		if assignyn == 'y' or assignyn == 'Y':
			assign()
			return None
		keeping = keeps()
		keep(keeping)
		yn = raw_input('input anything to roll')
		if yn:
			roll()
		self.table += self.hand
		self.hand = []
		print self.table
		print self.scorecard
		assign()
