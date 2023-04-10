# procedural orinted programming
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    print("Enter first number ")
    no1 = int(input())

    print("Enter second number ")
    no2 = int(input())

    Ans = add(no1,no2)
    print("Addition is : ",Ans)

    Ans = sub(no1, no2)
    print("Subtraction  is : ", Ans)

if __name__ == '__main__':
    main()