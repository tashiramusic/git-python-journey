# bubble sort

list_1 = [5, 2, 1, 8]

n = len(list_1)

for i in range(n - 1):
    for j in range(n - i - 1):
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]


print(list_1)
