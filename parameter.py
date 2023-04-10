# Positional Arguments  :in this type sequence is important
def Add1(No1,No2):
    print("Value of no1 : ",No1)
    print("Value of no2 : ",No2)
    return No1 + No2

def Sub(No1,No2):
    print("Value of no1 : ",No1)
    print("Value of no2 : ",No2)
    return No1 - No2

def main():
    ans = 0
    ans = Add1(10,11)
    print("Addition is :",ans)

    ans = Sub(No1=11,No2=10) #keyword argument
    print("Subtration is : " ,ans)

    ans = Sub(No2=11, No1=10)  # keyword argument
    print("Subtration is : ", ans)

if __name__ == '__main__':
    main()