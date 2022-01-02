l=[]
n =int(input("enter no of items"))
for x in range(n):
    v=int(input("enter values"))
    l.append(v)
print(l)

index=int(input("enter index"))
v=int(input("enter value for index"))
l.insert(index,v)
print(l)

for x in range(len(l)):
    print(l[x])
    print("list pop behaves as stack",l.pop())
print(l)
#pop - last in first out
