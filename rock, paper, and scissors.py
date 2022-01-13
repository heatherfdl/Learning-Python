# playing rock, paper, scissors game against the computer
#import random module
from random import randint #generates random outputs

# moves for the player
moves = ["rock", "paper", "scissors"]

# create a loop to play game over and over using 'while' loop
# true must always be spent with capital T
while True:
    computer = moves[randint(1,2)] # computer selects a move from list above random from positions 0 to 2 (ie rock to scissors)
    player = input("rock, paper, or scissors? (or end game?): ").lower()  #lowercases any input you enter
    if player == "end game":
        print("The game has ended. Play again soon!")
        break #breaks' while True' loop and the game ends
    elif player == computer: # elif is an extension onto the 'if' loop - essentially another 'if'
        print("Tie")
    elif player =="rock":
        if computer == "paper":
            print ("you lose", computer, "beats", player)
        else:
            print ("you win!", player, "beats", computer)
    elif player == "paper":
        if computer == "Scissors":
            print ("you lose", computer, "beats", player)
        else:
            print ("you win", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print ("you lose", computer, "beats", player)
        else:
            print ("you win", player, "beats", computer)
    else:
        print("check your spelling")


