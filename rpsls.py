
def game_logic(player1,p1_name,player2,p2_name):
	"""
		game_logic(str,str,str,str) -> str

		Receive players choice and machine choice with they respective name and return the winner

		>>>game_logic("rock","simon","scissors","Machine"):
		>>>rock crushes scissors so player simon wins

		>>>game_logic("spock","simon","lizard","Machine"):
		>>>lizard poisons spock so player Machine wins

		>>>game_logic("scissors","simon","scissors","Machine"):
		>>>it is a Tie
	"""
	if player1 == player2:
		return "it is a Tie"
	elif player1 == "rock":
		if player2 == "paper":
			return "paper cover rock so player "+p2_name+" wins"
		if player2 == "scissors":
			return "rock crushes scissors so player "+p1_name+" wins"
		if player2 == "lizard":
			return "rock crushes lizard so player "+p1_name+" wins"
		if player2 == "spock":
			return "spock vapourises rock so player "+p2_name+" wins"
	elif player1 == "paper":
		if player2 == "rock":
			return "paper cover rock so player "+p1_name+" wins"
		if player2 == "scissors":
			return "scissors cuts paper so player "+p2_name+" wins"
		if player2 == "lizard":
			return "lizard eats paper so player "+p2_name+" wins"
		if player2 == "spock":
			return "paper disproves spock so player "+p1_name+" wins"
	elif player1 == "scissors":
		if player2 == "paper":
			return "scissors cuts paper so player "+p1_name+" wins"
		if player2 == "rock":
			return "rock crushes scissors so player "+p2_name+" wins"
		if player2 == "lizard":
			return "scissors decapitates lizard so player "+p1_name+" wins"
		if player2 == "spock":
			return "spock smashes scissors so player "+p2_name+" wins"
	elif player1 == "lizard":
		if player2 == "scissors":
			return "scissors decapitates lizard so player "+p2_name+" wins"
		if player2 == "paper":
			return "lizard eats paper so player "+p1_name+" wins"
		if player2 == "rock":
			return "rock crushes lizard so player "+p2_name+" wins"
		if player2 == "spock":
			return "lizard poisons spock so player "+p1_name+" wins"
	elif player1 == "spock":
		if player2 == "lizard":
			return "lizard poisons spock so player "+p2_name+" wins"
		if player2 == "scissors":
			return "spock smashes scissors so player "+p1_name+" wins"
		if player2 == "paper":
			return "paper disproves spock so player "+p2_name+" wins"
		if player2 == "rock":
			return "spock vapourises rock so player "+p1_name+" wins"
	else:
		return "Enter a valid choice"

from random import randrange
machine_possible_choice = ["rock","paper","scissors","lizard","spock"]
machine_name = "Machine"
y_n = input("do you want to play?(y/n): ").lower()
player1_name = input("Enter your name: ")
while y_n == "y":
	player1_choice = input("Enter (rock or paper or scissors or lizard or spock): ").lower()
	machine_choice = machine_possible_choice[randrange(0,5)]
	winner = game_logic(player1_choice,player1_name,machine_choice,machine_name)
	print(winner)
	y_n = input("do you want to play again?: ")