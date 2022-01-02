#dictionary d={} d={k1:v1,k2:v2,k3:v3}

d={'2001':50,'2003':100,'2005':300,'2007':400}

key=input("enter key to get the value")
print("Value given by key is",d[key])

#when get key is used, code doesnt crash when key is not found - it prints none
if d.get(key)!=None:
    print("value for given key",d.get(key))
else:
    print("key doesn't exist")
key1=input("enter key to insert")
value= int(input("enter value for given key"))
d[key1]=value
print("dictionary after insertion",d)


          
