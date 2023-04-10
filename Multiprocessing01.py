
def DisplayEven(no):
    for i in range(1,no+1,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def DisplayOld(no):
    for i in range(1,no+1,1):
        if(i % 2 != 0):
            print("Odd number : ",i)


def main():
    print("Demostration of serial programming") # one by one process is execute
    DisplayEven(2000)
    DisplayOld(2000)


if __name__ == '__main__':
    main()