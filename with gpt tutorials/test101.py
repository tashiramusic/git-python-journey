"""
def personal():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    fav_hobby = input("Enter your favorite hobby: ")
    fav_lang = input("Enter your favorite programming language: ")
    print(f"Hello {name}! You are {age} years old and your favorite hobby is {fav_hobby}. Your favorite programming language is {fav_lang}.")

personal()


def check_adult():
    age = int(input("Enter Your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You're a child.") 
        
"""


def check_teen():
    age = int(input("Enter Your age: "))
    if age >= 18:
        print("You are an adult.")
    elif 13 <= age <= 17:
        print("You are a teenager.")
    else:
        print("You're a child.")

check_teen()