import yahtzee_categories as yc
import yahtzee_interface as yi
x1 = yc.ones([1,1,1,1,6])
x2 = yc.twos([2,2,1,2,6])
x3 = yc.threes([2,3,3,3,6])
x4 = yc.fours([2,1,1,1,6])
x5 = yc.fives([2,1,1,1,6])
x6 = yc.sixes([2,1,1,1,6])
	
while True:
	if yahtzee():
		assign score to yahtzee()
	else:
		if largeStraight():
			assign score to largeStraight()
		else:
			if smallStraight():
				assign score to smallStraight()
			else:
				if fullHouse():
					assign score to fullHouse():
				else:
					if fourOfAKind():
						assign score to fourOfAKind():
					else:
						if threeOfAKind():
							assign score to threeOfAKind()
						else:
							if x1>2:
								yi.assign() score to yc.ones()
							else:
								if x2>2:
									yi.assign() score to yc.twos()
								else:
									if x3>2:
										yi.assign() score to yc.threes()
									else:							
										if x4>2:
											yi.assign() score to yc.fours()
										else:
											if x5>2:
												yi.assign() score to yc.fives()
											else:
												if x6>2:
													yi.assign() score to yc.sixes()