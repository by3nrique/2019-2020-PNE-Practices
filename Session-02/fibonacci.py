a = 0
b = 1
total = 0
while total <= 55:
    print(total, end=" ")
    total = (b + a)
    b = a
    a = total
