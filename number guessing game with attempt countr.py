import random

random_int = random.randint(1, 10)
# print(random_int)

attempt_count = 0

while True:
    user_input = int(input("Enter a number between 1 to 10: "))

    attempt_count = attempt_count + 1

    if user_input > random_int:
        print("TOO High")
    elif user_input < random_int:
        print("TOO Low")
    else:
        print("You guessed correctly!")
        print("Congratulations")
        print(f"You took {attempt_count} attempts")
        break
