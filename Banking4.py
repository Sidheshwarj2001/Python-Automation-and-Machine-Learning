# Instance variable = name, account, address ,accountNo
# instance method  : CreateAccount( ) DisplayAccount()
# class variable =  Bank_Name , ROI_On_FD
# class method : DisplayBankInformation()
# static method : DisplayKYCInfo

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

    @staticmethod
    def DisplayKYCInfo():
        print("Plase consider below KYC information : ")
        print("According to the rule of Goverment of india you have to submit below documents")
        print("1.clear and recent password size photo")
        print("2.photoof adhar card")
        print("3.Photo of PAN card")

    def Deposite(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():
    print("___________________Banking Application____________________")

    print()
    print("_______________Calling Static method to Diplay KYC info______________")

    BankAccount.DisplayKYCInfo()

    print()
    print("____________Accessing the instance variable from main______________")

    print("Name of Bank : ",BankAccount.Bank_Name)
    print("Rate of Intrest on Fixed Desposite : ",BankAccount.ROI_On_FD)

    print()
    print("________________Calling the class method to diplay bank information ______")
    BankAccount.DisplayBankInformation()

    print()
    print("Crating the object of the class")

    Customer1 = BankAccount()
    Customer2 = BankAccount()

    print()
    print("___________Creating the first account___________")
    print("____________Enter Details for fist account_______")
    Customer1.CreateAccount()

    print()
    print("___________Creating the second account___________")
    print("____________Enter Details for second account_______")
    Customer2.CreateAccount()

    print()
    print("__________calling instance method to display information of first Account____________ ")
    Customer1.DisplayAccountInfo()

    print()
    print("__________calling instance method to display information of first Account____________ ")
    Customer2.DisplayAccountInfo()

    Customer1.Deposite(10000)
    Customer2.Deposite(20000)

    print("Amount of {} user1 after deposite is  {}: ".format(Customer1.Name,Customer1.Amount))
    print("Amount of {} user1 after deposite is  {}: ".format(Customer2.Name,Customer2.Amount))
    print()
    print("____________withdraw 2000 in customer 1")

    Customer1.Withdraw(2000)

    print()
    print("____________withdraw 2000 in customer 1")

    Customer2.Withdraw(5000)

    print("Amount of {} after withdraw is {}: ".format(Customer1.Name, Customer1.Amount))
    print("Amount of {} after withdraw is {}: ".format(Customer2.Name, Customer2.Amount))


print("_____________Thank you______________________________")




if __name__ == "__main__":
    main()