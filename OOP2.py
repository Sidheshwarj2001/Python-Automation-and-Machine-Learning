
class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()

    def Accept(self):
        print("How many element you want to store? ")
        self.size = int(input())

        print("Please Enter the elements : ")
        for i in range(0,self.size):
            value = int(input())
            self.Arr.append(value)


    def Display(self):
        print("Element of list are : ")
        for i in range(0,self.size):
            print(self.Arr[i])

    def Addition(self):
        sum = 0
        for i in self.Arr:
            sum = sum + i

        print("sum of list of element is : ",sum)

def main():

    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Addition()

if __name__ == "__main__":
    main()