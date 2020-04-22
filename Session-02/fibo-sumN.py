# This functions return the sum of the N terms of de fibonacci sequence
def fibosum(n):
    a = 0
    b = 1
    rest = 0
    for count in range(0, n):  # Range includes every number from 1 to n
        c = (b + a)
        rest = rest + c
        b = a
        a = c
    return rest


# -- Print the calculations
print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))
