

def main():
    print("Enter number of rows : ")
    num =  int(input())

    for i in range(0,num):
        for j in range(i,num):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    main()