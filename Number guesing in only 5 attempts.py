# for i in range(1, 6):
#    print(i)
#    if i == 5:
#        print("Game over")
#
#
import random

random_int = random.randint(1, 10)

for i in range(1, 10):
    user_input = int(input("Enter a number between 1 to 10: "))
    if i != 5:
        if user_input > random_int:
            print("TOO High")
        elif user_input < random_int:
            print("TOO Low ")
        else:
            print("You guessed it correctly!")
            break
    else:
        print("Game Over!")
        print(f"The Number was {random_int}.")
        break
