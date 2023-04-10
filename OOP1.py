
class Arithematic:

    def __init__(self,A,B):  #specialvariable
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans

def main():
    print("inside main method")

    obj = Arithematic(10,11)
    output = obj.Addition()
    print("Addition is : ",output)
    output = obj.Subtraction()
    print("Subtraction is : ",output)


if __name__ == " __main__":
    print("Inside the starter")
    main()
