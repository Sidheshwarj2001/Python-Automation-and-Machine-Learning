print("Application to Demostrate Industrial Programming")

def main():
    print("Enter first number : ")
    no1 = input()
    print(type(no1))

    print("enter second Number : ")
    no2 = input()
    print(type(no2))

    ans = int(no1) + int(no2)
    print("Addition is : ",ans)

if __name__ == "__main__":
    main()