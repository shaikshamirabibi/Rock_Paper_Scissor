import random

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

while True:

    user = input("Enter rock, paper or scissor: ").lower().strip()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissor.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)


    if user == computer:
        print("Match Draw")

    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("User Wins")
        user_score += 1

    else:
        print("Computer Wins")
        computer_score += 1

    print("User Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\nFinal Score:")
        print("User Score:", user_score)
        print("Computer Score:", computer_score)

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Computer won the game!")
    else:
        print("The game is a draw!")

    break
