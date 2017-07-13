import yahtzee_categories as yc
import yahtzee_interface as yi

def main():
	P1 = yi.Player()
	P2 = yi.Player()
	for i in range(13):
		print("Player 1's Turn!")
		P1.move()
		print("Player 2's Turn!")
		P2.move()
	P1Score = getTotalScore(P1.scorecard)
	P2Score = getTotalScore(P2.scorecard)
	print("Player 1 has earned " + str(P1Score) + " points!")
	print("Player 2 has earned " + str(P2Score) + " points!")
	if P1Score > P2Score:
		print("Player 1 has won the game!")
	elif P2Score > P1Score:
		print("Player 2 has won the game!")
	else:
		print("Game is a draw!")

if __name__ == "__main__":
	main()
	while raw_input("Would you like to play again? (y/n)\n") == "y":
		main()
