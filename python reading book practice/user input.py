#num_1 = 0
#num_2 = 0

def add():
  #  global num_1
   # global num_2
    
    #get first number
    result_1 = input("Enter a number: ")

    num_1 = 0

    for digit_1 in result_1:
        num_1 = num_1 * 10 + (ord(digit_1) - ord('0'))

    #print the type of first number
    print(type(num_1))




    #get second number
    result_2 = input("Enter a number_2: ")

    num_2 = 0

    for digit_2 in result_2:
        num_2 = num_2 * 10 + (ord(digit_2) - ord('0'))

    print(type(num_2))

    #now addition these two numbers
    addtion = num_1 + num_2
    print("So the answer is.....")
    print(addtion)
    print(type(addtion))





add()