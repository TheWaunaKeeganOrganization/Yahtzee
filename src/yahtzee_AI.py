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
			print self.table
			select, maxP = self.compute_move(self.table)
			# print "select :", select, "maxP :", maxP
			if rolls < 3:
				assignyn = self.assigndecision(maxP)
				if assignyn == 'y' or assignyn == 'Y':
					self.assign(select)
					print "Assigning to :", select
					assigned = True
					return None
				else:
					keeping = self.keeps()
					print "keeping :", keeping
					# print keeping
					self.keep(keeping)
		if not assigned:
			self.assign(select)
			print "Assigning to :", select

	def keeps(self):
		highC, highN = self.getdups()
		if eval('smallStraight')(self.table) != 0 and self.scorecard['largeStraight'] == None:
			return self.straight()
		keeping = []
		for i in range(highC):
			keeping.append(highN)
		return keeping

	def compute_move(self, tab):
		# print self.scorecard
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
		if eval('smallStraight')(self.table) != 0 and self.scorecard['largeStraight'] == None:
			return 'n'
		for i in ['largeStraight', 'fullHouse', 'yahtzee']:
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
			# print "maxP :",maxP, "average :", maxVal/count
			return 'n'
		return 'n'

	def getTotalScore(self):
		total = 0
		for i in self.scorecard.keys():
			total += self.scorecard[i]
		bonuscalc = 0
		for j in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']:
			bonuscalc += self.scorecard[j]
		if bonuscalc >= 63:
			total += 35
			print "got bonus"
		return total

	def getdups(self):
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
			if i[1] > 3:
				highC = i[1]
				highN = i[0]
			elif i[1] == 3 and (self.scorecard['threeOfAKind']  == None or self.scorecard['fourOfAKind'] == None):
				highC = i[1]
				highN = i[0]
			elif i[1] > highC and i[0] in plausible:
				highC = i[1]
				highN = i[0]
		if highC == 2:
			highN = 0
			for i in dups:
				if i[0] > highN:
					highN = i[0]
		return highC, highN

	def straight(self):
		count = 0
		for i in [1,2,3,4]:
			if i in self.table:
				count += 1
		if count == 4:
			return [1,2,3,4]
		count = 0
		for i in [2,3,4,5]:
			if i in self.table:
				count += 1
		if count == 4:
			return [2,3,4,5]
		count = 0
		for i in [3,4,5,6]:
			if i in self.table:
				count += 1
		if count == 4:
			return [3,4,5,6]
		return None