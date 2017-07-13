import itertools, random, sys, copy
import yahtzee_scorecard as ys
from yahtzee_categories import *

class Player:
	def __init__(self):
		self.scorecard = ys.Scorecard(self)
		self.hand = []
		self.table = ["1","1","1","1","1"]
		
	def roll(self):
		self.table = list(random.choice(list(itertools.product(range(1,7),repeat = len(self.table)))))
		self.table += self.hand
		self.hand = []
		print self.table

	def keep(self, keepers):
		for n in keepers:
			self.table.remove(n)
			self.hand.append(n)

	def assign(self):
		print self.scorecard
		assignment = raw_input('To which category do you wish to assign them (see the above scorecard):\n')
		if assignment in self.scorecard.emptySpace():
			self.scorecard.update(assignment, self.table)
		else:
			print 'Point category is already taken'
			self.assign()

	def keeps(self):
		print self.table
		inputted = raw_input('Which dice do you want to keep (comma separated numbers): \n').split(',')
		k = map(lambda x: int(x) if x in "123456" else "Fail",inputted)
		tab = copy.deepcopy(self.table)
		for n in k:
			if n in tab:
				tab.remove(n)
			else:
				print 'That is not a valid input'
				return self.keeps()
		return k

	def move(self):
		raw_input('Input anything to roll\n')
		self.roll()
		assignyn = raw_input('Do you want to assign your points to a category? y/n:\n')
		if assignyn == 'y' or assignyn == 'Y':
			self.assign()
			return None
		keeping = self.keeps()
		self.keep(keeping)
		raw_input('Input anything to roll\n')
		self.roll()
		assignyn = raw_input('Do you want to assign your points to a category? y/n:\n')
		if assignyn == 'y' or assignyn == 'Y':
			self.assign()
			return None
		keeping = self.keeps()
		self.keep(keeping)
		raw_input('Input anything to roll\n')
		self.roll()
		self.assign()
