import random
R=0
P=1
S=2
while True:
    player = input("Enter your choice(rock,paper,scissors):")
    variables ={R:"rock",P:"paper",S:"scissors"}
    computer = random.choice(variables)
    print(f"\nPlayer {player}: computer {computer}.\n")

    #checking for a winner

    if player == computer:
        print(f"You both selected {player}. It's a draw!")
    elif player =="rock":
        if computer == "scissors":
            print("Rock beat scissors, player won!")
        else:
            print("paper covers rock! player lose!")
    elif player == "paper":
        if computer == "rock":
         print("paper covers rock player won!")
        else :
         print("you lose, computer wins!")
    elif player == "scissors":
        if computer =="paper":
            print("player win!, computer lose!")
        else:
            print("computer wins!, player lose")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
