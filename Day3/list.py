#List L= []

l=[1,2,3,4]
l[0]=10
print(l)
l.append(8)
print(l)
l1=l #both l and l1 point towards the same object
l2=l.copy() #a new object is formed having the same elements
print(l1,"id of l1",id(l1))
print(l,"id of l",id(l))
print(l2,"id of l2",id(l2))

l.append(9)
print(l)
print(l1) #9 present
print(l2) #no 9

l=[]
n =int(input("enter no of items"))
for x in range(n):
    v=int(input("enter values"))
    l.append(v)
print(l)

for x in range(len(l)):
    print(l[x])
