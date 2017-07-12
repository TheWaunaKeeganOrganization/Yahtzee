import yahtzee_categories as yc
# import yahtzee_interface as yi

def main():
	# Will be uncommented when yahtzee_interface is implemented
	# P1 = yi.Player()
	# P2 = yi.Player()
	# for i in range(13):
	# 	P1.move()
	# 	P2.move()
	# P1Score = getTotalScore(P1.scorecard)
	# P2Score = getTotalScore(P2.scorecard)
	# if P1Score > P2Score:
	# 	print("Player 1 has won the game!")
	# elif P2Score > P1Score:
	# 	print("Player 2 has won the game!")
	# else:
	# 	print("Game is a draw!")
	pass


if __name__ == "__main__":
	main()
	while raw_input("Would you like to play again? (y/n)\n") == "y":
		main()
