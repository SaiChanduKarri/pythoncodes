a = input()
li = []
for i in a:
    li.append(i)
    if i.isnumeric():
        for i in range(int(i)):
            li.append('*')
print(''.join(li))