b=input()
a = list(b)
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i].upper(),end='')
    else:
        print(a[i].lower(),end='')
