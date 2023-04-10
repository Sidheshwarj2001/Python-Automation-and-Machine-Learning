
def ChkNum(no):

    if(no %2==0):
        return "Even Number"

    else :
        return "Old Number"

def main():

    print("Enter a first number 1: ")
    num1 = int(input())

    print(ChkNum(num1))


if __name__ == "__main__":
    main()