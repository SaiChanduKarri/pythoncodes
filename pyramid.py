a = int(input())
b = (a * 2)-1
c = 0
d = b //2
for i in range(0,a):
    for j in range(0,b):
        if ( j >= d - c and  j <=  d + c ):
            print("*",end="")
        else:
            print(" ",end="")
    c = c+1
    print()


