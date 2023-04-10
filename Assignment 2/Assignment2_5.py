def checkPrime(no):
    if(no>1):
        for i in range(2,int(no/2)+1):
            if (no%i==0):
                return "It is a not prime number"
            else:
                return "It is prime number"
    else:
        return "it is not prime number"


def main():

    print("Enter a number")
    num = int(input())

    print(checkPrime(num))

if __name__ == "__main__":
    main()
