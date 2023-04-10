# function which accept nothing and return nothing
def Demo1():
    print("Inside Demo1")

# function accepts one parameter and return nothing
def Demo2(No):
    print("Inside Demo 2 with argument : ",No)

# function Accept one parameter and return one parameter
def Demo3(No):
    print("Inside Demo3 with argument : ",No)
    return  No +2

# function accept two parameter and return one parameter
def Demo4(no1,no2):
    print("Inside Demo 4 ")
    Add = no1+no2
    return Add

# function accept two parameter and return two parameter
def Demo5(no1,no2):
    print("Inside Demo 5 ")
    Add = no1 + no2
    sub = no1-no2
    return Add,sub  #it return list


def main():
    Demo1()

    Demo2(11) #give any type of data

    ans = Demo3(11)
    print("Return value of Demo3 is :",ans)

    Ans = Demo4(10,21)
    print("Return value is :",Ans)

    Ans1,Ans2 = Demo5(21,11)
    print("First return value is : ", Ans1)
    print("Second return value is : ", Ans2)

    # print(type(Demo5(21,11))





if __name__ == "__main__":
    main()
