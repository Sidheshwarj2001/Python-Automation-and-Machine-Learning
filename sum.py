# lets make software for atm machine
class Atm():
    def __init__(self):
        self._balance = 0  # declare variable or attribute
        self._pin = ''
        # constructor ahe: __init__()

    #         self.menu()

    def menu(self):
        user_input = input('''
                Welcome to Atm
                how would you like to proceed?
                Enter 1 for Generate/create pin
                Enter 2 for Deposite money
                Enter 3 for withdraw money
                Enter 4 for check the balance
                Enter 5 to exist     


''')
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposite()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.exist()

    def create_pin(self):
        self._pin = input("enter your new pin:")
        print("your Atm pin set successfully.......")

    def get_pin(self):  # getter method
        return self._pin

    def set_pin(self):  # setter method
        new_pin = input("enter your new pin ...:")
        if type(new_pin) == str:
            self._pin = new_pin
            print('pin set succesfully...')

    def deposite(self):
        temp = input("enter ATM pin : ")
        if temp == self._pin:
            amount = int(input("enter amount : "))
            self._balance = self._balance + amount
            print("Deposite sucessful...!")
        else:
            print("Wrong pin.....!")

    def withdraw(self):
        temp = input("enter ATM pin : ")
        if temp == self._pin:
            amount = int(input("enter Amount :"))
            if amount < self._balance:
                self._balance = self._balance - amount
                print("withdraw sucessfully.....!")
            else:
                print('insufficient Balance in your accound....!')
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter ATM pin : ")
        if temp == self._pin:
            print("your balance is :", self._balance)
        else:
            print("invalid pin")

    def exist(self):
        print("Exist sucessfully")


sbi = Atm()
# sbi.create_pin()
# sbi.deposite()
# id(sbi)