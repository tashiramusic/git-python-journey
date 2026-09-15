questions = [
    "What is the capital of Sri Lanka?",
    "What language are we learning?",
    "How many bits are in a byte?",
    "What does CPU stand for?",
    "What symbol is used for comments in Python?",
]

right_ans = 0
wrong_ans = 0

answers = ["colombo", "python", "8", "central processing unit", "#"]

rounds = len(questions)
mcq_no = 0
ans_no = 0

print("===== Python Quiz =====")

while mcq_no < rounds:
    print(questions[mcq_no])

    user_ans = str(input("Type answer: ".lower()))

    if user_ans == answers[ans_no]:
        print("Right")
        right_ans = right_ans + 1

    else:
        print("Wrong")
        print(f"The answer is {answers[ans_no]}")

    mcq_no = mcq_no + 1
    ans_no = ans_no + 1

print("Quiz finished!")
print(f"Your Score: {right_ans}/{rounds} ")
