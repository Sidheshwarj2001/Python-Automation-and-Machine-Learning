
def Add(no1,no2):
    return no1 + no2


def main():

    print("Enter a first Number : ")
    num1 = input()
    print("Enter a second Number : ")
    num2 = input()

    result = Add(int(num1),int(num2))

    print(result)




if __name__ == "__main__":
    main()