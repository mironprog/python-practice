import random

choices = ['rock', 'paper', 'scissors']

player_choice = None

while player_choice not in choices:
    player_choice = input("Write your choice:").lower()

print("The player chosed: "+str(player_choice))


comps_choice = random.choice(choices)
print("The computer chosed: "+comps_choice)

if comps_choice == player_choice:
    print("It's a tie!")
elif comps_choice == "rock" and player_choice == "scissors":
    print("The computer won!")
elif comps_choice == "paper" and player_choice == "rock":
    print("The computer won!")
elif comps_choice == "scissors" and player_choice == "paper":
    print("The computer won!")
else:
    print("The player won!")



