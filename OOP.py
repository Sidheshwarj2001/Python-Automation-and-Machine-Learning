# object oriented programming

# problem  : Accept two number and perform addition and subtraction of it

# class  = characteristics  + Behaviours
# class = Data + Functions

# he don question vicharche

# kay karaycha  ?  ----> Behaviour (Functions)

# te karaysathi kashachii garaj ahe ---->Characterstic(Data)

class Arithematic :  # no1,no2 characterstic and a,b is parameter
    def __init__(self,A,B):
        self.No1  = A
        self.No2 = B

    def Add(self): # Behaviour (function)
        return self.No1 + self.No2

    def sub(self):
        return self.No1 - self.No2

def main():
    print("Enter first number ")
    value1 = int(input())

    print("Enter second number ")
    value2 = int(input())

    obj = Arithematic(value1,value2)

    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.sub()
    print("Addition is : ", Ans)

if __name__ == '__main__':
    main()