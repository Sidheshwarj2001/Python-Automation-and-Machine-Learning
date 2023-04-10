print("Application to Demostrate Industrial Programming")

def addition(value1,value2):   #it is generic function
    ans = value1 + value2
    return ans

def main():
    print("Enter first number : ")
    no1 = int(input())
    print("enter second Number : ")
    no2 =int(input())

    sum = addition(no1 , no2)
    # print()
    print("Addition is : ",sum)

if __name__ == "__main__":
    main()