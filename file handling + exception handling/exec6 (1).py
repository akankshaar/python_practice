class PintuException(Exception):
    def __init__(self,msg):
        print("Pintu exception :",msg)



def validateAge(age):
    if age<18:
        raise PintuException("invalid age")
    else:
        print("valid age")


a=int(input("enter age"))
validateAge(a)
    
    
