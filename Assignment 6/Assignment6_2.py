class BankName:
    ROI= 10.5
    def __init__(self):
        self.Name = input("\nEnter your name : ")
        self.Amount = int(input("Enter Amount in you Account : "))


    def Display(self):
        print("\nName : ",self.Name)
        print("Amount in your Account : ",self.Amount)

    def Deposite(self):
        self.Amount += int(input("\nEnter Amount You want to Deposite : "))
        # self.Amount - amount

    def Withdraw(self):
        self.Amount-= int(input("\nEnter Amount you want to withdraw : "))
        # self.Amount-WithdrawAmount

    def CalculateInterest(self):
        rateOfIntrest = (BankName.ROI * self.Amount *12 ) / 100
        print("Rato of interest on your amount is per year is  :",rateOfIntrest)


def main():
    Customer1 = BankName()
    Customer1.Deposite()
    Customer1.Withdraw()
    Customer1.Display()
    Customer1.CalculateInterest()


    Customer2 = BankName()
    Customer2.Deposite()
    Customer2.Withdraw()
    Customer2.Display()
    Customer2.CalculateInterest()

    Customer3 = BankName()
    Customer3.Deposite()
    Customer3.Withdraw()
    Customer3.Display()
    Customer3.CalculateInterest()

if __name__ == "__main__":
    main()