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

	def keep(self, keepers):
			for n in keepers:
				self.table.remove(n)
				self.hand.append(n)


	def assign(self, select):
		# print "\n" + select + ":",
		# print eval(select)(self.table + self.hand), "\n"
		self.scorecard[select] = eval(select)(self.table + self.hand)
		# for i in self.scorecard.keys(): print i, ":", self.scorecard[i], "\n"


	def move(self):
		rolls = 0
		assigned = False
		while rolls < 3 and not assigned:
			self.roll()
			rolls += 1
			if len(self.hand) != 0:
				self.table += self.hand
				self.hand = []
			# print self.table
			select, maxP = self.compute_move(self.table)
			if rolls < 3:
				assignyn = self.assigndecision(maxP)
				if assignyn == 'y' or assignyn == 'Y':
					self.assign(select)
					assigned = True
					return None
				else:
					keeping = self.keeps()
					# print keeping
					self.keep(keeping)
		self.assign(select)

	def keeps(self):
		plausible = []
		dups = []
		for i in self.scorecard.keys():
			if self.scorecard[i] == None:
				if i == 'ones':
					plausible.append(1)
				elif i == 'twos':
					plausible.append(2)
				elif i == 'threes':
					plausible.append(3)
				elif i == 'fours':
					plausible.append(4)
				elif i == 'fives':
					plausible.append(5)
				elif i == 'sixes':
					plausible.append(6)

		for i in self.table:
			if self.table.count(i) >= 2:
				dups.append((i,self.table.count(i)))
		highC = 0
		highN = 0
		for i in dups:
			if i[0] > 3:
				highC = i[1]
				highN = i[0]
			elif i[0] == 3 and self.scorecard["largeStraight"] == None:
				highC = i[1]
				highN = i[0]
			elif i[1] > highC and i[1] in plausible:
				highC = i[1]
				highN = i[0]
		if highC == 2:
			highN = 0
			for i in dups:
				if i[0] > highN:
					highN = i[0]
		keeping = []
		for i in range(highC):
			keeping.append(highN)
		return keeping

	def compute_move(self, tab):
		possibility = {}
		for i in self.scorecard.keys():
			if self.scorecard[i] == None:
				possibility[i] = eval(i)(tab)
		maxVal = -1
		cat = None
		for i in possibility.keys():
			if possibility[i] > maxVal:
				maxVal = possibility[i]
				cat = i
		return cat, maxVal

	def assigndecision(self, maxP):
		for i in ['smallStraight', 'largeStraight', 'fullHouse', 'yahtzee']:
			if self.scorecard[i] != None:
				if eval(i)(self.table) != 0:
					return 'y'
		keeping = self.keeps()
		tab = copy.deepcopy(self.table)
		hand = []
		for n in keeping:
				tab.remove(n)
				hand.append(n)
		pos = itertools.permutations(range(1,6),len(tab))
		maxVal = 0
		count = 0
		for i in pos:
			temp = []
			count += 1
			for j in i:
				temp.append(j)
			temp += hand
			cat, point = self.compute_move(temp)
			maxVal += point
		if maxP < (maxVal/count):
			print "maxP :",maxP, "average :", maxVal/count
			return 'n'
		return 'n'

	def getTotalScore(self):
		total = 0
		for i in self.scorecard.keys():
			total += self.scorecard[i]
		return total
