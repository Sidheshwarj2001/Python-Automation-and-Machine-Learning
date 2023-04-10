

def Divisible(no):
    if(no%5==0):
        return "True"
    else:
        return "False"

def main():

    print("Enter a Number: ")
    num1 = input()

    result = Divisible(int(num1))

    print(result)


if __name__ == "__main__":
    main()
