def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 2

def filterX(arr, Function_Name):
    Result = []
    for no in arr:
        if (Function_Name(no)):
            Result.append(no)
    return Result

def mapX(arr, function_name):
    result = []

    for no in arr:
        value = function_name(no)
        result.append(value)
    return result

def reduceX(arr):
    sum = 0
    for no in arr:
        sum = sum + no
    return sum

def main():
    Data = [2, 3, 1, 6, 4, 5]

    print("Original data : ", Data)
    Data_filter = list(filterX(Data, CheckEven))
    print("Data after Filter : ", Data_filter)

    Data_map = list(mapX(Data_filter, Increment))
    print("Data after map : ", Data_map)

    Ret = reduceX(Data_map)
    print("Data after reduce :", Ret)

if __name__ == '__main__':
    main()
