class Atm():  # creating class
    #     Contructor :-it is a function inside a class
    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.menu()

    def menu(self):
        user_input = input("""
        hi how i help you?
        1.press 1 for creating pin
        2.press 2 for to change pin
        3.press 4 for withdraw
        4.press 3 for check balance
        5. exist
        """)

        if user_input == "1":
            # create pin
            self.create_pin()

        elif user_input == "2":
            # change pin
            self.change_pin()

        elif user_input == "4":
            # withdraw
            self.withdraw()

        elif user_input == "3":
            self.check_balance()

        else:
            exit()

    def create_pin(self):
        setpin = input("Enter your new pin ")
        conformpin = input("Confirm your pin Again ")

        if setpin == conformpin:
            self.pin = conformpin
            print("Your ATM pin set successfully")
            self.menu()
        else:
            print('Enter same pin ERROR : .......')

    def change_pin(self):
        setpin = input("Enter your first pin ")

        if setpin == self.pin:
            newpin = input("Enter your new pin ")
            print("Your new pin set successfully  ")
            self.pin = newpin
            self.menu()
        else:
            print("pin nahi kar de sakta re babba...")

    def check_balance(self):
        Checkpin = input("Enter your pin ")

        if Checkpin == self.pin:
            print("your Balance is : ",self.balance)
            self.menu()
        else:
            print("PIN is incorrect ")

    def withdraw(self):
        checkpin = input("enter you pin ")

        if checkpin == self.pin:
            amount = int(input("Enter the Amount "))
            if amount < self.balance:
                print("Payment is processing ")
                self.balance -= amount
                print("Withdraw successufully.....")

            else:
                print("INSUFFICEIENT BALANCE ")
        else:
            print("PIN IS INCORRECT")
        self.menu()


def main():
    person1 = Atm()  # creating object
if __name__ == "__main__":
    main()
