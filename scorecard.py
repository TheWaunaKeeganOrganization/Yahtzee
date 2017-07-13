import yahtzee_categories

class Scorecard():
	def __init__(self):
		self.scores = {}
		self.upperScoreKind = ["ones", "twos", "threes", "fours", "fives", "sixes"]
		self.lowerScoreKind = ["threeOfAKind", "fourOfAKind", "fullHouse", "smallStraight", "largeStraight", "yahtzee", "chance"]
		for name in self.upperScoreKind:
			self.scores[name] = -1
		for name in self.lowerScoreKind:
			self.scores[name] = -1
		self.scores["bonus"] = 0

	def __str__(self):
		upperSum = sum([self.scores[name] for name in self.upperScoreKind if self.scores[name]>=0])
		scoreTuple = tuple([self.scores[i] if self.scores[i]>=0 else 0 for i in self.upperScoreKind])+(upperSum,self.scores["bonus"])+\
					 tuple([self.scores[i] if self.scores[i]>=0 else 0 for i in self.lowerScoreKind])+(self.getTotalScore(),)
		s = """
-------------------
Ones:			%3d
Twos:			%3d
Threes:			%3d
Fours:			%3d
Fives:			%3d
Sixes:			%3d
-------------------
Sum:			%3d
Bonus:			%3d
-------------------
Three of a kind:%3d	
Four of a kind:	%3d
Full House:		%3d
Small straight:	%3d
Large straight:	%3d
Chance:			%3d
YHATZEE:		%3d
-------------------
TOTAL SCORE:	%3d
""" %scoreTuple

		return s
		
	# list of unfilled score names
	def emptySpace(self):
		upper = [name for name in upperScoreKind if self.scores[name]==-1]
		lower = [name for name in lowerScoreKind if self.scores[name]==-1]
		return upper + lower

	# current total score
	def getTotalScore(self):
		return sum([self.scores[name] for name in self.scores if self.scores[name]>=0])

	# given scoreKind and dices, update self.scores based on the 
	def update(self, scoreKind, rolls):
		assert(self.scores[scoreKind] == -1)
		scoreFunc = getattr(yahtzee_categories, scoreKind)
		self.scores[scoreKind] = scoreFunc(rolls)

		# if upper sum is greater or equal to 63, then the bonus score becomes 35
		upperSum = sum([self.scores[name] for name in self.upperScoreKind if self.scores[name]>=0])
		if upperSum >= 63: self.scores["bonus"] = 35

if __name__ == '__main__':
	card = Scorecard()
	card.update("ones", [1, 1, 1, 2, 2])
	card.update("twos", [1, 1, 1, 2, 2])
	card.update("threes", [3, 3, 3, 3, 2])
	card.update("fours", [4, 4, 4, 4, 2])
	card.update("fives", [5, 5, 6, 5, 5])
	card.update("sixes", [6, 6, 6, 6, 2])
	print card.getTotalScore()
	print card