
def EvenOld(no):

    if(no>0):
        return "Positive Number"
    elif(no<0):
        return  "Negative Number"
    else:
        return "Zero"

def main():

    print("Enter a number : ")
    num1 = input()

    result = EvenOld(int(num1))

    print(result)


if __name__ == "__main__":
    main()