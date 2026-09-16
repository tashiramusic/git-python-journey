### Find the Second Largest Number in a List ###
numbers = [10, 20, 4, 45, 99]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)
print("The first largest number is:", numbers[-1])
print("The second largest number is:", numbers[-2])