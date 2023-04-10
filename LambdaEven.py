def checkEven(No):
    if(No%2==0):
        return  "EVEN"
    else:
        return "OLD"

def CheckEvenX(No):
    return (No%2==0)

EvenLambda = lambda  No : ChceckEvenX(No)

def main():

    print(checkEven(10))
    print(CheckEvenX(12))

    print(EvenLambda)

if __name__ == '__main__':
    main()