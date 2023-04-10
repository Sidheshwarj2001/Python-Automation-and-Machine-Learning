
def main():
    print("Enter a size  of list : ")

    sizeList  = int(input())

    Arr = list()

    print()

    for i in range(0,sizeList,1):

        value = input()

        Arr.append(value)
        
        # Arr.insert(i,value)  #another way

    print()

    print("our List is :",Arr)


if __name__ == "__main__":
    main()