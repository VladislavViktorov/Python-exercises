n = int(input("Enter number:"))
print(bin(n))
m = int(input("Enter the bit:"))
if n & (1 << m):
    print(1)
else:
    print(0)
