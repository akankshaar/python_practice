a = float (input("Enter a value of base"))
b = float (input("Enter a value of height"))
print(0.5*a*b)

s = int(input("Enter selling price"))
c = int(input("Enter cost price"))

'''if s>c :
    print ("profit% = ",((s-c)*100/c)
    else
    print ("loss% = ",((c-s)*100/c) '''

#while loop
i = 0
while i<10:
    print(i)
    i = i+1
    print("Value of i after termination",i)


#table

a = int(input("Enter a number : "))
print ("Table of", a ,"is")

i = 1
while i<=10:
    print (a, "*",i,"=",a*i)
    i = i+1

#While loop stops only when a certain number "n" is entered
a = input("Enter a : ")
while a!='n':
    print("Value is",a)
    a= input("Enter n to exit or press any key to continue")

#another way to solve previous query
'''while(1):
    c = input('enter a string")
          if c =='n':
          break '''
#For loop [for var in iterator(range)] body
for x in range(5,15):
    print(x)

#another example
n = int(input("Enter number = "))
for x in range(1,11):
    n1 = n*x
    print(n1)

#To find a number divisible by both 4 and 5
for x in range (100,500):
    if x%4 ==0 and x%5==0 :
        print (x)

#To get each letter of the word hello

'''s = "hello"
for i in s
print(i)'''

#other method

s = input("Enter a string : ")
for x in range (len(s)):
    print (s[x])

#other method

s = "Hello"
s[0]
s[1]

#Pattern 1

for x in range(3):
    for y in range (3):
        print ("*",end="  ")
    print()

#Pattern 2
for x in range(3):  #for number of rows
    for y in range (x+1):  #for number of columns when x = 0 , y =1 (1 star)
        print("*",end = " ")
    print()




    
    
