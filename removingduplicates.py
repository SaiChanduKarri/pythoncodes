a = input()
b = list(a)
c = []
for i in b:
    if i not in c:
        c.append(i)
print(''.join(c))


