print("####Number Guessing Game####")

import random


random_no = random.randint(1, 100)
# print(random_no)

while True:
    user_input = int(input("Enter A number to guess 1 to 100: "))

    if user_input > random_no:
        print("Too high")
    elif user_input < random_no:
        print("too low")
    else:
        print("You guess correcly....")
        print("Congratulations!")
        break
