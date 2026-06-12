import random

choices = ["rock", "paper", "scissor"]

count_user = 0
computer_number_of_wins = 0

while True:

    user = input("Enter rock, paper or scissor: ")
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Match Draw")

    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("User Wins")
        count_user += 1

    else:
        print("Computer Wins")
        computer_number_of_wins += 1

    print("User Score:", count_user)
    print("Computer Score:", computer_number_of_wins)

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        break