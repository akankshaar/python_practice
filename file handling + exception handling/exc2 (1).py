def div():
    try:
        a=int(input("enter a number"))
        b=int(input("enter a number 2"))
        c=a/b
        print(c)
    except ValueError:
        print("enter only int type values")
        div()
    except Exception as e:
        print("exception name is ",e)
        print("enter value except zero")
        div()
    


div()
