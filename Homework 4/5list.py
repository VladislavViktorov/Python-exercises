n = int(input())
l = list()
for k in range(n):
    l.append(k)
m = int(input())
for y in range(0, len(l)):
    if m == 0 and l[y] % 2 == 0:
        l[y] += 5
    if m == 1 and l[y] % 2 != 0:
        l[y] += 5
print(l)
