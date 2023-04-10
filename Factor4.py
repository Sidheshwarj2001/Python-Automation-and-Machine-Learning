
def DisplayFactor(num):
    i = 1

    print("Factors are : ")

    while (i <= int(num / 2)):
        if (num % i == 0):
            print(i)
        i += 1


def main():

    print("Enter a number")
    no = int(input())

    DisplayFactor(no)

if __name__ == "__main__":
    main()

