def div():
    try:
        a=int(input("enter a number"))
        b=int(input("enter a number 2"))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("divide by zero not possible")
        print("enter value except zero")
        div()
    except ValueError:
        print("enter only int type values")
        div()
    else:
        print("else run")


div()
