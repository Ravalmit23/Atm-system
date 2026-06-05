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
        

a1=atm()
a1.menu()