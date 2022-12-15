n = int(input())
d = {}
for i in range(n):
    key = input()
    value = input()
    d[key] = value
m = int(input())

l = []

for i in range(m):
    l.append(input())

for i in range(len(l)):
    if l[i] in d.keys():
        a = l[i]
        l[i] = d[l[i]]
        d.pop(a)

print(d)
print(l)
