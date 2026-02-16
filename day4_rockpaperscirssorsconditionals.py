import random #importing class random to use function choice of class random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
player=input("Rock, Paper, or Scissors ").lower()
print("Computer choice: {}".format(computer))
if(player==computer):
    print("Tie!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")