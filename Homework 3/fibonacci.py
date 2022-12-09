n = int(input("Enter number: "))
a = 0
b = 1
for i in range(n):
    x = a
    a = b
    b = x+b
    print(a)
