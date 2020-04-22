# -- Main program (print the fibonacci sequence until 55)
a = 0
b = 1
total = 0
while total <= 55:
    print(total, end=" ")  # Print the information in the same line
    total = (b + a)
    b = a
    a = total
