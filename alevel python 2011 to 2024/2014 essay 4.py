# Factorial of a positive integer n is defined 
#as n x (n-1) x (n-2) x ....... x 3 x 2 x 1.

n = 5
minus = 1
factorial = 0

for i in range(n):
#    print(i)
    if i == 0:
        factorial = n
    else:
        factorial = factorial * (minus)
        minus = minus + 1
    print(factorial)

print("The factorial of {} is {}".format(n,factorial))


