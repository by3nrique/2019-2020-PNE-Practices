# This functions return the Nth term of de fibonacci sequence
def fibonacci(n):
    a = 0
    b = 1
    c = 0
    for count in range(0, n):  # Range includes every number from 1 to n
        c = (b + a)
        b = a
        a = c
    return c


# -- Print the calculations

print("5th Fibonacci term:", fibonacci(5))
print("10th Fibonacci term:", fibonacci(10))
print("15th Fibonacci term:", fibonacci(15))
