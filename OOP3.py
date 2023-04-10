

class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()

    def Accept(self):
        print("how many element you want to : ")
        self.size  = int(input())

        for i in range(0,self.size,1):
            value = 0
            print("Enter a element : ")
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print("our element are : ")
        for i in self.Arr:
            print(i)

    def Addition(self):
        sum = 0
        for i in self.Arr:
            sum = sum + i

        print("Sum of element is : ",sum)


def main():

    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Addition()

if __name__ == "__main__":
    main()