# perfect number programe

class Value:

    def __init__(self,Data):
        self.No = Data

    def SumFactors(self):
        sum = 0
        for i in range(1,int(self.No/2)+1):
            if(self.No%i==0):
                sum = sum+i
        return sum

    def checkPerfect(self):
        ans = self.SumFactors()

        if(self.No == ans):
            return True
        else:
            return False

def main():
    print("please enter number : ")
    A = int(input())

    obj = Value(A)

    ret = obj.checkPerfect()
    if ret == True:
        print("{} is a perfect number ".format(A))
    else:
        print("{} is not a perfect number ".format(A))

if __name__ == "__main__":
    main()