#Tuple - immutable, size cannot be modified t= ( ) , slicing can be done
#tuple(l) can be used to covert a list to tuple as typle cannot be modified

t1=(1,2,3)
print(t1)
type(t1)

t1[0]
t1[0:]
t1[ : : -1]

#unpacking
x,y,z =t
print(x)
print(y)
print(z)

s="hello"
tuple(s)

l=[1,2,3,4]]
tuple(1)

#swap1
x=10
y=10
z=x
x=y
y=z

#swap2
(x,y)=(y,x)

#swap3
x,y,z =10,20,30
