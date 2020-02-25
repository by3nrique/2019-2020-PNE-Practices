def fibonacci(n):
    a = 0
    b = 1
    total = 0
    for e in range(0, n):
        total = (b + a)
        b = a
        a = total
    return (total)


print("5th Fibonacci term:", fibonacci(5))
print("10th Fibonacci term:", fibonacci(10))
print("15th Fibonacci term:", fibonacci(15))
