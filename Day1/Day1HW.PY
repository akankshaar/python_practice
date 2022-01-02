#pattern 3
for x in range(3):
    for y in range(3-x): #as rows increasing star decreasing
        print("*",end = " ")
    print()


#pattern 4
for x in range(1,4):
    for y in range(1,x+1):
        print(y, end = " ")
    print()

    
#pattern 5
num = 1
for x in range(1,4):
    for y in range(1,x+1):
        print(num, end = " ")
        num= num+1
    print()


#pattern 6

'''for x in range(4,1,-1):
    for y in range(1,4):
        if y<x-1:
            print(" ",end=" ")
        else :
            print(*)
    print()'''
            

#To check if prime or not

num = int(input("Enter a number"))

if num>1:
    for i in range(2,num):
        if num%i == 0 :
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
    print()


#Factorial

n= int(input("Enter the number = "))
result = 1
for i in range(n,0,-1):
    result = result*i
print("Factorial of n is ",result)

#Reverse of a number
a= int(input("enter a number = "))
rev=0
while a>0:
    reminder=a%10
    rev=(a*10)+reminder
    a=a//10
print("Reverse of the number is",%rev)5
