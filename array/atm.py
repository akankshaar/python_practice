Print("Welcome to the SBI Bank ATM")
chances=3
restart=('y')
balance= 67000

while chances>=0:
    pin=int(input("Please enter your pin"))
    if pin == (1234):
        print("You entered the pin correctly")
        restart=input("Do you wish to restart?")
        while restart not in ('n','no','N','NO'):
            print("Please press 1 for your balance")
            print("Please press 2 to make a withdrawl")
            print("Please press 3 to know your balance")
            print("Please press 4 to exit")

            if option == 1:
                print("Your balance is 67000")
                restart=input("Do you wish to restart?")
                if restart in('n','no','N','NO'):
                    print("Thank you")
                    break
            elif option == 2:
                withdrawl=float(input("How much money do you want to withdraw?"))
                if withdrawl in [100,200,500,2000]:
                    balance=balance-withdrawl
                    print("Your balance is now ",balance)
                    restart=input("Do you wish to restart?")
                    if restart in ('n','no','N','NO'):
                        print("Thank you")
                        break
                elif withdraw != [100,200,500,2000]:
                    print("Invalid amount, try again")
                    restart="y"
            elif option == 3:
                Pay_in=float(input("How much would you like to deposit?"))
                balance=balance+pay_in
                print("Your balance is ",balance)
                restart=input("Do you wish to restart?")
                    if restart in ('n','no','N','NO'):
                        print("Thank you")
                        break
            elif option == 4:
                print("Thank you for visiting!")
            else:
                print("Please enter a correct number")
                restart=("y")
        elif pin!= ('1234'):
            print("Incorrect password")
            chances=chances-1
            if chances==0:
                print("No more tries ")
                break
