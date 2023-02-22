import random
from termcolor import colored

labels = ["rock","paper","scissor"]

while True:
    computer = random.choice(labels)
    player = None
    while player not in labels:
        player = input("Choose: rock,paper or scissor? : ").lower()
    print("Player: "+ player)
    print("Computer: "+ computer)

    if computer == player:
        print("-----Tie-----")
    elif player =="rock" and computer =="scissor":
        print("----- Player Wins ---")
    elif player =="paper" and computer =="rock":
        print("Player Wins")
    elif player =="scissor" and computer =="paper":
        print("Player Wins")
    else:
        print("Computer Wins")

    play_again = input("Do you want to play again, enter (y): ").lower()
    print("\n")
    if play_again != "y":
        break

print('Thank You For Playing     Bye!...Bye!')