from functools import reduce

class Numbers:
    Data = []

    def __init__(self):
        self.value = int(input("Enter number : "))

    def ChkPrime(self):
        for i in range(2,self.value,1):
            if(self.value % i == 0):
                return False

            else:
                return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.value):
            if (self.value % i == 0):
                sum = sum + i
        if (sum == self.value):
            return True
        else:
            return False

    def Factors(self):
        for i in range(1,int(self.value/2)+1,1):
            if(self.value % i == 0):
                print(i)
                Numbers.Data.append(i)

    def SumFactors(self):

        result = reduce(lambda a,b : a+b ,Numbers.Data)
        print(result)

def main():
    obj1 = Numbers()
    obj1.ChkPrime()
    obj1.ChkPerfect()
    obj1.Factors()
    obj1.SumFactors()

    obj2 = Numbers()
    obj2.ChkPrime()
    obj2.ChkPerfect()
    obj2.Factors()
    obj2.SumFactors()

    obj3 = Numbers()
    obj3.ChkPrime()
    obj3.ChkPerfect()
    obj3.Factors()
    obj3.SumFactors()

if __name__ == "__main__":
    main()