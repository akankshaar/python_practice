#strip and count function

web=input("enter a web url")
item=input("enter item to count")
ss=web.strip('w')
sl=web.lstrip('w')
sr=web.rstrip('w')
print("web url after strip",ss)
print("web url after left strip",sl)
print("web url after right strip",sr)
print("Count given item in web",web.count(item))
