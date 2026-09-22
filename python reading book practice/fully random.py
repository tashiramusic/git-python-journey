import random

arr = []
ran_range = random.randint(2,10)

count = 0

def genarate_random_list():
    for num in range(ran_range):
        ran = random.randint(1,100)
        arr.append(ran)
    print(arr)

def find_length():
    global count
    for item in arr:
        count = count + 1
    print(count)

genarate_random_list()
find_length()