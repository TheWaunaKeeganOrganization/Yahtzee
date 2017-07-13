import itertools, random, sys, copy
from yahtzee_categories import *
class Player:
	def __init__(self):
		self.scorecard = {}
		self.hand = []
		self.table = ["1","1","1","1","1"]
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
		for i in self.scorecard.keys(): print i, ":", self.scorecard[i], "\n"
		assignment = raw_input('To which category do you wish to assign them (see the above scorecard):\n')
		try:
			if assignment != None:
				print eval(assignment)(self.table + self.hand)
				self.scorecard[assignment] = eval(assignment)(self.table + self.hand)
			else:
				raise 'myerror'
		except:
			print 'point assignment is not valid'
			self.assign()

	def keeps(self):
		print self.table
		input = raw_input('Which dice do you want to keep (ex. for a roll of [5,4,3,4,6], you could write 4,4): \n')
		try :
			if len(input) > 0:
				k = map(int, input.split(','))			
			else: k = []
		except:
				print 'That is not a valid input'
				return self.keeps()
		tab = copy.deepcopy(self.table)
		for n in k:
			if n in tab:
				tab.remove(n)
			else:
				print 'That is not a valid input'
				return self.keeps()
		return k

	def move(self):
		rolls = 0
		assigned = False
		while rolls < 3 and not assigned:
			raw_input('Input anything to roll\n')
			if True:
				self.roll()
				rolls += 1
				if len(self.hand) != 0:
					self.table += self.hand
					self.hand = []
			print self.table
			if rolls < 3:
				assignyn = raw_input('Do you want to assign your points to a category? y/n:\n')
				while assignyn not in ['y', 'Y', 'n', 'N']:
						print 'That is not a valid input'
						assignyn = raw_input('Do you want to assign your points to a category? y/n:\n')
				if assignyn == 'y' or assignyn == 'Y':
					self.assign()
					assigned = True
					return None
				else:
					keeping = self.keeps()
					self.keep(keeping)
		self.assign()
