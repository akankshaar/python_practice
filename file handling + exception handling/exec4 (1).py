def div():
    try:
        try:
            a=int(input("enter a number"))
            b=int(input("enter a number 2"))
            c=a/b
            print(c)
        except ValueError:
            print("value error")
            div()
            
       
    except ZeroDivisionError:
        print("divide by zero not possible")
        print("enter value except zero")
        div()
   


div()
