def additionOfDigit(no):
    sum = 0
    for i in str(no):
        sum = sum + int(i)

    print("Sum is :",sum )

def main():

    print("Enter a number ")
    num = int(input())

    additionOfDigit(num)


if __name__ == '__main__':
    main()