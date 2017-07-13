import itertools, random, sys, copy
from yahtzee_categories import *
class AI:
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

	def assign(self, select):
		print "\n" + select + ":",
		print eval(select)(self.table + self.hand), "\n"
		self.scorecard[select] = eval(select)(self.table + self.hand)
		for i in self.scorecard.keys(): print i, ":", self.scorecard[i], "\n"


	def move(self):
		rolls = 0
		assigned = False
		while rolls < 3 and not assigned:
			self.roll()
			rolls += 1
			if len(self.hand) != 0:
				self.table += self.hand
				self.hand = []
			print self.table
			select, maxP = self.compute_move()
			if rolls < 3:
				assignyn = self.assigndecision(maxP)
				if assignyn == 'y' or assignyn == 'Y':
					self.assign()
					assigned = True
					return None
				else:
					keeping = self.keeps()
					print keeping
					self.keep(keeping)
		self.assign()

	def keeps(self):
		dups = []
		for i in self.table():
			if self.table.count(i) >= 2:
				dups.append((i,self.table.count(i)))
		highC = 0
		highN = 0
		for i in dups:
			if dups[i][1] > highC:
				highC = dups[i][1]
				highN = dups[1][0]
		if highC == 2:
			highN = 0
			for i in dups:
				if dups[i][0] > highN:
					highN = dups[i][0]
		keeping = []
		for i in dups:
			if dups[i][0] == highN:
				keeping.append(highN)
		return keeping

	def compute_move(self):
		possibility = {}
		for i in self.scorecard.keys():
			if self.scorecard[i] == None:
				possibility[i] = eval(i)(self.table + self.hand)

		print possibility
		maxVal = -1
		cat = None
		for i in possibility.keys():
			if possibility[i] > maxVal:
				maxVal = possibility[i]
				cat = i
		return cat, maxVal

	def assigndecision(self, maxP):
		for i in ['smallStraight', 'largeStraight', 'fullHouse', 'yahtzee']:
			if self.scorecard[i] != None
				if eval(i)(self.table + self.hand) != 0:
					return 'y'

		return 'n'

	def getTotalScore(self):
		total = 0
		for i in self.scorecard.keys():
			total += self.scorecard[i]
		return total
