def main():

    print("Enter a number")
    num = int(input())

    print("Factors are : ")
    i=1
    while(i<=int(num/2)):
        if(num % i ==0):
            print(i)
        i+=1

if __name__ == "__main__":
    main()

