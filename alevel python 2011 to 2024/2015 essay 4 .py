marks_and_name = {}

def input_name_marks():
    name = input("Input you name: ")
    marks = []

    for mark in range(3):
        num = int(input("Enter mark: "))
        if num == -1:
            marks_and_name.clear()
            break
        else:
            if num >= 0 and num <=100:
                marks.append(num)
        

    marks_and_name[name] = marks
    print(marks_and_name)


#append to text file

def append_to_txt():
    with open("alevel python 2011 to 2024/example.txt", "a") as file:
        file.write(str(marks_and_name) +"\n")
        print("Marks saved")
        file.close()

input_name_marks()
append_to_txt()