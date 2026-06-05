class atm:
    def __init__(self):
        self.pin=''
        self.balance=10000
    def menu(self):
        print('''
        PRESS 1:CREATE PIN
        PRESS 2:UPDATE PIN
        PRESS 3:CHECK BALANCE
        PRESS 4:WITHDRAW AMOUNT
        PRESS 5:DEPOSIT AMOUNT
        PRESS 6:EXIT
              ''')
        user_choice=int(input("enter your choice:"))
        if user_choice==1:
            self.create_pin()
            self.menu()
        elif user_choice==2:
            self.update_pin()
            self.menu()
        elif user_choice==3:
            self.check_balance()
            self.menu()
        elif user_choice==4:
            self.withdraw()
            self.menu()
        elif user_choice==5:
            self.deposit()
            self.menu()
        else:
            exit()

    #atm methods

    def create_pin(self):
        atm_pin=int(input("ENTER THE PIN:"))
        self.pin=atm_pin
        print("YOUR PIN CREATED SUCCESSFULLY")

    def update_pin(self):
        pin1=int(input("ENTER YOUR OLD PIN:"))
        if pin1==self.pin:
            new_pin=int(input("ENTER YOUR NEW PIN:"))
            self.pin=new_pin
            print("PIN UPDATED SUCCESSFULLY")
        else:
            print("OOPS! ENTER VALID PIN")
    def check_balance(self):
        atm_pin=int(input("enter your pin:"))
        if atm_pin==self.pin:
            print("YOUR BALANCE=",self.balance)
        else:
            print("you enter wrong pin")
    def withdraw(self):
        pin2=int(input("enter your pin="))
        if pin2==self.pin:
            withdraw1=int(input("enter your withdraw amount="))
            if withdraw1>self.balance:                      #nested if 
                print("unsufficient balance")
            else:
                self.balance=self.balance-withdraw1
                print("after withdrawal your balance=",self.balance)
    def deposit(self):
        pin3=int(input("enter your pin="))
        if pin3==self.pin:
            deposit=int(input("enter your deposit amount="))
            self.balance=self.balance+deposit
            print("after deposit your balance=",self.balance)
        

        
        

        
        

a1=atm()
a1.menu()