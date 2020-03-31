a = int(input("enter a value:"))
b = int(input("enter a value:"))
l = []
l.extend((a,b))
print(l)
li = []
li.append(a)
li.append(b)
print(li)
print( sum(li) )
print("the sum is:",sum(l))
 # Two methods