# any .py file contain function u can shared it is called module

print("Application to Demostrate Industrial Programming")

import MarvellousModule

def main():
    print("value of __name__ from main is :", __name__)
    print("Enter first number : ")
    no1 = int(input())
    print("enter second Number : ")
    no2 =int(input())

    sum = MarvellousModule.addition(no1 , no2)
    # print()
    print("Addition is : ",sum)

if __name__ == "__main__":
    main()


# print(type(main()))