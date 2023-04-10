def main():

    print("Enter a number")
    num = int(input())

    print("Factors are : ")
    for i in range(1,num,1):
        if num % i ==0:
            print(i)
            i+=1

if __name__ == "__main__":
    main()

