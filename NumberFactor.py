def DisplayFactor(num):
    i = 1

    print("Factors are : ")

    while (i <= int(num / 2)):
        if (num % i == 0):
            print(i)
        i += 1