
def Area(Redius,PI):
    Result = PI * Redius * Redius
    return Result

def Area(Redius,PI=3.14): #default parameter
    Result = PI * Redius * Redius
    return Result

def Area1(Redius,PI):
    Result = PI * Redius * Redius
    return Result

def main():
    RValue = 10.5
    PIvalue = 3.14
    Ans = Area(RValue,PIvalue) #keyword argument Ans = Area(10.5,3.14)
    print("Area of circle :" ,Ans)

    Ans = Area(10.5)  # default argument Ans = Area(10.5) #default and positionalṇṇ
    print("Area of circle :", Ans)

    # keyword + Defualt
    Ans = Area1(PI = 7.10,Redius=10.5)
    print("Area of Circle : ",Ans)


if __name__ == '__main__':
    main()