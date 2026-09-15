# bubble sort

list_1 = [5, 2, 1, 8]

count = 0

for i in list_1:
    if list_1[count] > list_1[count + 1]:
        list_1[count + 1] = list_1[count]
    count = count + 1


print(list_1)
