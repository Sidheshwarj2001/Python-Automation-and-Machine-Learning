# Applicationn to find out the maximum number

def maximum(value1,value2):

    if(value1>value2):
        return value1
    else:
        return value2


def main():

    print("Enter a first number")
    num1 =input()

    print("Enter a second number")
    num2 = input()

    Ans =  maximum(int(num1),int(num2))
    print("Largest number is : ",Ans)

if __name__ == "__main__":
    main()