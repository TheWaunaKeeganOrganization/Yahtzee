import yahtzee_categories

class Scorecard():
	def __init__(self):
		#self.player = player
		self.scores = {}
		self.upperScoreKind = ["ones", "twos", "threes", "fours", "fives", "sixes"]
		self.lowerScoreKind = ["threeOfAKind", "fourOfAKind", "fullHouse", "smallStraight", "largeStraight","chance", "yahtzee"]
		for name in self.upperScoreKind:
			self.scores[name] = -1
		for name in self.lowerScoreKind:
			self.scores[name] = -1
		self.scores["bonus"] = -1

	def __str__(self):
		upperSum = sum([self.scores[name] for name in self.upperScoreKind if self.scores[name]>=0])
		scoreTuple = tuple([self.scores[i] if self.scores[i]>=0 else 0 for i in self.upperScoreKind])+(upperSum,self.scores["bonus"])+\
					 tuple([self.scores[i] if self.scores[i]>=0 else 0 for i in self.lowerScoreKind])+(self.getTotalScore(),)
		posScoreTuple = {k:(v if v>-1 else "Taken") for k,v in yahtzee_categories.allCategories(self.player.table).iteritems()}
		s = """
CAT 			CUR 	POS
-----------------------------------
ones:			%03d	{0[ones]}
twos:			%03d	{0[twos]}
threes:			%03d	{0[threes]}
fours:			%03d	{0[fours]}
fives:			%03d	{0[fives]}
sixes:			%03d	{0[sixes]}
-----------------------------------
sum:			%03d
bonus:			%03d
-----------------------------------
threeOfAKind:		%03d	{0[threeOfAKind]}
fourOfAKind:		%03d	{0[fourOfAKind]}
fullHouse:		%03d	{0[fullHouse]}
smallStraight:		%03d	{0[smallStraight]}
largeStraight:		%03d	{0[largeStraight]}
chance:			%03d	{0[chance]}
yahtzee:		%03d	{0[yahtzee]}
-----------------------------------
TOTAL SCORE:		%03d
""".format(posScoreTuple) %scoreTuple 

		return s
		
	# list of unfilled score names
	def emptySpace(self):
		upper = [name for name in self.upperScoreKind if self.scores[name]==-1]
		lower = [name for name in self.lowerScoreKind if self.scores[name]==-1]
		return upper + lower

	# current total score
	def getTotalScore(self):
		return sum([self.scores[name] for name in self.scores if self.scores[name]>=0])

	def getUpperScore(self):
		return sum([self.scores[name] for name in self.upperScoreKind if self.scores[name]>=0])		

	def isUpperFull(self):
		return reduce(lambda x,y:x and y, [self.scores[name]>=0 for name in self.upperScoreKind])

	# given scoreKind and dices, update self.scores based on the 
	def update(self, scoreKind, rolls):
		assert(self.scores[scoreKind] == -1)
		scoreFunc = getattr(yahtzee_categories, scoreKind)
		self.scores[scoreKind] = scoreFunc(rolls)

		# if upper sum is greater or equal to 63, then the bonus score becomes 35
		upperSum = sum([self.scores[name] for name in self.upperScoreKind if self.scores[name]>=0])
		if self.isUpperFull():
			self.scores["bonus"] = 35 if upperSum >= 63 else 0

if __name__ == '__main__':
	card = Scorecard()
	card.update("ones", [1, 1, 1, 2, 2])
	card.update("twos", [1, 1, 1, 2, 2])
	card.update("threes", [3, 3, 3, 3, 2])
	card.update("fours", [4, 4, 4, 4, 2])
	card.update("fives", [5, 5, 6, 5, 5])
	card.update("sixes", [6, 6, 6, 6, 2])
	print card.getTotalScore()
	print card.isUpperFull()