def Add(*values):
    print(type(values))
    print("Number of Argument",len(values))
    print("Values is :" , values)

    sum = 0

    for no in values:
        sum = sum + no
    return sum

def Addx(*values):
    sum = 0

    for i in range(0,len(values)):
        sum = sum + i

    return sum

def main():
    Ans = Add(10,20,20,20,30,40)
    print("Addition is : ",Ans)

    Ans1 = Addx(1,2,2,2,3,4)
    print("Addition is : ",Ans1)

if __name__ == '__main__':
    main()