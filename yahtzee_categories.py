from collections import Counter

def ones(d):
	return 1*d.count(1)

def twos(d):
	return 2*d.count(2)

def threes(d):
	return 3*d.count(3)

def fours(d):
	return 4*d.count(4)

def fives(d):
	return 5*d.count(5)

def sixes(d):
	return 6*d.count(6)

def threeOfAKind(d):
	if max(Counter(d).itervalues())>=3:
		return sum(d)
	return 0

def fourOfAKind(d):
	if max(Counter(d).itervalues())>=4:
		return sum(d)
	return 0

def fullHouse(d):
	if (list(Counter(d).itervalues())[0]==3 and list(Counter(d).itervalues())[1]==2) or (list(Counter(d).itervalues())[0]==2 and list(Counter(d).itervalues())[1]==3):
		return 25
	return 0

def smallStraight(d):
	s=min(d)
	if s+1 in d and s+2 in d and s+3 in d:
		return 30
	return 0

def largeStraight(d):
	s=min(d)
	if s+1 in d and s+2 in d and s+3 in d and s+4 in d:
		return 30
	return 0

def yahtzee(d):
	if d.count(d[0])==5:
		return 50
	return 0

def chance(d):
	return sum(d)

def allCategories(d):
	scores={}
	scores["ones"]=ones(d)
	scores["twos"]=twos(d)
	scores["threes"]=threes(d)
	scores["fours"]=fours(d)
	scores["fives"]=fives(d)
	scores["sixes"]=sixes(d)
	scores["threeOfAKind"]=threeOfAKind(d)
	scores["fourOfAKind"]=fourOfAKind(d)
	scores["fullHouse"]=fullHouse(d)
	scores["smallStraight"]=smallStraight(d)
	scores["largeStraight"]=largeStraight(d)
	scores["yahtzee"]=yahtzee(d)
	scores["chance"]=chance(d)
	return scores
	
	print scores