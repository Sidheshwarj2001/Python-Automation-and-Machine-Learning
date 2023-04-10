# Instance variable = name, account, address ,accountNo
# instance method  : CreateAccount( ) DisplayAccount()
# class variable =  Bank_Name , ROI_On_FD
# class method : DisplayBankInformation()

class BankAccount:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_On_FD = 6.7

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

    @classmethod
    def DisplayBankInformation(cls):
        print("\n__________________Welcome to our Banking Console________________\n")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposit is : ",cls.ROI_On_FD)
        print()

def main():
    print("Name of Bank : ",BankAccount.Bank_Name)
    print("Rate of Intrest on Fixed Desposite : ",BankAccount.ROI_On_FD)

    BankAccount.DisplayBankInformation()

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