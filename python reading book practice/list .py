int_list = [1, 2, 3]
string_list = ['abc', 'defghi']

empty_list = []

empty_list.append(int_list)
empty_list.append(string_list)

#error haddle part
try:
    print(empty_list[2])
except:
    IndexError
    print("List out of range brother")
    print(empty_list)
