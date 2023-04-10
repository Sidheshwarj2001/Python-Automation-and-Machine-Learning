def factor(no):
    sum = 0

    print("Sum is : ")
    for i in range(1,int(no/2)+1,1):
        if i%2==0:

            sum =sum+i

    return sum

def main():

    print("Enter one Number : ")
    num = int(input())

    print(factor(num))

if __name__ == "__main__":
    main()
