print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("enter player 1's choice: ").strip().lower()
print("***** No Cheating *****\n\n" * 20)

player2 = input("enter player 2's choice: ").strip().lower()

if player1 == player2:
	print("Its a tie!")

elif player1 == "rock":
	if player2 == "scissors":
		print("rock beats scissors, Player 1 wins")
	elif player2 == "paper":
		print("paper covers rock, player 2 wins")

elif player1 == "scissors":
	if player2 == "paper":
		print("scissors cuts paper, player 1 wins")
	if player2 == "rock":
		print("rock smashes scissors, player 2 wins")

elif player1 == "paper":
	if player2 == "rock":
		print("paper covers rock, player 1 wins")
	if player2 == "scissors":
		print("scissors cuts paper, player 2 wins")

else:
	print("Something went wrong")
