class atm:
    def __init__(self):
        pin=''
        balance=10000
    def menu(self):
        print('''
        PRESS 1:CREATE PIN
        PRESS 2:UPDATE PIN
        PRESS 3:CHECK BALANCE
        PRESS 4:WITHDRAW AMOUNT
        PRESS 5:DEPOSIT AMOUNT
        PRESS 6:EXIT
              ''')
        user_choice=input("enter your choice:")
        if user_choice=='1':
            self.create_pin()
            self.menu()
        elif user_choice=='2':
            self.update_pin()
        elif user_choice=='3':
            pass
        elif user_choice=='4':
            pass
        elif user_choice=='5':
            pass
        else:
            exit()
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

        
        

        
        

a1=atm()
a1.menu()