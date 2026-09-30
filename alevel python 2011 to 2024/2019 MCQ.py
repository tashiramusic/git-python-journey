i = 8
result = 1


while True:
    number = int(input("Enter a num: "))

    #check number
    if number<=0:
        i = i -1
    else:
        result = result * number
        i = i - 1

    #if i is 0 program will break
    if i<=0:
        break

print(result)