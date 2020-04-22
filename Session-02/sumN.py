# Function for calculating the sum of the
# N first integer numbers


def sumN(N):
    total_sum = 0
    for number in range(1, N + 1):  # Range includes every number from 1 to N + 1
        total_sum += number  # add each number to the total sum
    return total_sum


# Print the calculations
print("Sum of the 20 first integers: ", sumN(20))
print("Sum of the 100, frist integers: ", sumN(100))
