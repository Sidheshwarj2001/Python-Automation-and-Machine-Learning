# Instance variable = name, account, address ,accountNo
# instance method  : CreateAccount( ) DisplayAccount()

class BankAccount:

    def __init__(self):
        self.Name = ""
        self.Amount = 0.0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your Name : ")
        self.Name = input()

        print("Enter your intial Amount : ")
        self.Amount = float(input())

        print("Enter your Addresss : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("\n______________your Account Information is below______________\n")
        print("Name of Account Holder  : ",self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in Account : ",self.Amount)
        print("\n__________________Thank You___________________\n")

def main():

    Customer1 = BankAccount()
    Customer2 = BankAccount()

    print("Account no 1 ")
    Customer1.CreateAccount()
    print("Account no 2")
    Customer2.CreateAccount()

    Customer1.DisplayAccountInfo()
    Customer2.DisplayAccountInfo()

if __name__ == "__main__":
    main()