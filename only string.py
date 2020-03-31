a = input()
li = []
for i in a:
    if( (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
        li.append(i)
print(''.join(li))