# marks = {"Alice":[90, 85, 92], "Bob":[78, 82, 88], "Charlie":[95, 90, 93]}

import os

marks ={}

def func():
    name = input("Enter your name:")
    scores = []

    
    for i in range(3):
        score = int(input("Enter your score: "))
        if score == -1:
            clear_marks()
            break
        elif score >= 0 and score <= 100:
            scores.append(score)
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
            return

    marks[name] = scores



def save_marks():
    with open("alevel python 2011 to 2024/example.txt", "a") as file:
        file.write(str(marks) + "\n")
        print("Marks saved to example.txt")
        file.close()

def clear_marks():
    marks.clear()
    print("Marks cleared.")


func()
save_marks()