import random

"""
choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Choose rock, paper, or scissors or exit: ")

print("Computer chose:", computer)
"""

while True:
    choices = ["rock", "peper", "scissors"]
    computer = random.choice(choices)

    user = input("choose rock,peper or scissors: ").lower()

    if computer == user:
        print(f"Computer choose {computer}")
        print("tie")

    elif computer == "rock" and user == "peper":
        print(f"computer choose {computer} ")
        print("User win")
        exit_var = input("Do you want to exit (Y/N): ").lower()
        if exit_var == "y":
            break

    elif computer == "scissors" and user == "rock":
        print(f"computer choose {computer} ")
        print("User win")
        exit_var = input("Do you want to exit (Y/N): ").lower()
        if exit_var == "y":
            break

    # User wins

    elif computer == "peper" and user == "scissors":
        print(f"computer choose {computer} ")
        print("User Win")
        exit_var = input("Do you want to exit (Y/N): ").lower()
        if exit_var == "y":
            break
    else:
        print(f"computer choose {computer} ")
        print("Computer Win")
        exit_var = input("Do you want to exit (Y/N): ").lower()
        if exit_var == "y":
            break

    # User wins
