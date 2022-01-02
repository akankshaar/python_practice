.#strings

s=input("Enter string")
sl = s.lower()
su = s.upper()
st = s.title()
sw= s.swapcase()

print("Lower case",sl)
print("Upper case",su)
print("Standard case",st)
print("swapcase",sw)

item=input("Enter string")
print("first occurence of character",s.find(item))
print("last occurence of character",s.rfind(item))
print("index",s.index(item))

