#dictionary

number=int(input("Insert the number for the items"))
d={ }
for i in range(number):
    key=int(input("Insert the key"))
    value=input("Insert the value")
    d[key]=value
print("Dicionary = ",d)
print("keys of dictionary are",d.keys())
for k in d.keys():
    print("key",k)

print("values of dictionary are",d.values())
for v in d.values():
    print("values",v)

print("items for dictonary are:",d.items())
for i in d.items():
    print("items",i)

for k in d.items():
    print("item = ",k, "key = ",k[0],"value = ",k[1])

#pop returns value and popitem returns both key and value
    
k = input("enter key to pop")
print("dictionary item pop",d.pop(k))
print("dictionary after pop item is ", d.popitem())

#to copy one dictionary to another
d1=d.copy()
print(d1)

#to clear a dictionary
d1.clear()
print(d1)

#to merge two dictionaries
d2=("1":10,"2":20,"3":30)
d.update(d2)
print(d)

#a key can havve multiple values and nesting of dictionary can also be done
d5={'2001':[10,20,30],cl:{'2002':200,'2004':400},'2005':500,'2006':600}
for k in d5.keys():
    print(k)
for v in d5.values():
    print(v)
    for x in v.values():
    print(x)
