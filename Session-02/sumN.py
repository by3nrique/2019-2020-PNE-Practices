# Function for calculating the sum of the
# N first integer numbers


def sumN(n):
    rest = 0
    for i in range(1, n + 1):
        rest += i
    return rest


# -- The main program starts here
print("Sum of the 20 first integers: ", sumN(20))
print("Sum of the 100, frist integers: ", sumN(100))
