def name_parts():

    while True:

        full_name = input("Enter your full name here: ")

        #split into list
        full_name = full_name.split()

        #lengh of parts
        length_of_name = len(full_name)
    #  print(length_of_name)

        if length_of_name ==2:
            print("Valid name")
            print("")
            break
        elif length_of_name == 1:
            print("include last name too....")
        else:
            print("")
            print("The name can have only two part like first_name and last_name")
            print("")

    




#call the function
name_parts()