l =['abc','aba','cba','121']
str=0

for word in len(l):
    if word>2 and word[0]==word[-1]:
        str=str+1
print(str)
