# single burner

def square(No):
    return No*No

def main():
    Data = [1,2,3,4,5]
    Result = []

    for Value in Data:
        Result.append(square(Value))

    print("Result after square operation is : ",Result)

if __name__ == '__main__':
    main()