#sort function

l=[100,1,50,200,10]
l.sort
print(l)

#Descending
l.sort(reverse=True)
print(l)

l=['aa','aac','aabc']
l.sort()
print(l)

#Sorting string
l.sort(key=len) #sorts on the basis of length of the string
print(l)
l.sort(key=len, reverse=True)
print(l)


#normal reverse
l.reverse()
print(l)
