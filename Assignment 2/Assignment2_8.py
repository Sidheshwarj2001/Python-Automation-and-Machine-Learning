
def main():

    num = int(input("Enter a number : "))

    for i in range(0,6):
        for j in range(1,i+1):
            print(j,end=' ')
        print()


if __name__ == "__main__":
    main()