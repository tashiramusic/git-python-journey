"""
a = 4
b = 4.7
c = a + b

print(c) #8.7
print(type(c)) #<class 'float'>

"""


"""
total = 0.0
x = float(input("Enter a number:"))
while x > 0:
    total = total + x
    x = float(input("Enter a number:"))
print(total) 

"""
# Prints the sum of all positive numbers entered by the user.

#You are requested to write a Python program to find and display the maximum value of
#given 10 integers. The program should read integers one at a time.



array = [55,25,100,99,101]
#largest_2 = max(array)
largest = array[0]

for i in array:
    if largest < i:
        largest = i

print(largest)
#print(largest_2)


