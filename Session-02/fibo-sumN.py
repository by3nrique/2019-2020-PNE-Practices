def fibosum(n):
    a = 0
    b = 1
    rest = 0
    for e in range(0, n):
        c = (b + a)
        rest = rest + c
        b = a
        a = c
    return rest


print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))
