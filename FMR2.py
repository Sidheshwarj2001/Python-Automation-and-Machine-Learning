
def CheckEven(No):
    return (No % 2 == 0)

def multipllyByTwo(No):
    return No*2

def sum(a,b):
    return a+b

def filterX(Helper_function,Data):
    result = []
    for no in Data:
        if(Helper_function(no)==True):
            result.append(no)

    return result

def mapX(Helper_Function,Data):
    result = []
    for no in Data:
        value = Helper_Function(no)
        result.append(value)

    return result

def reduceX(Helper_Function,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)

    return Ans

def main():
    print("Enter number of element you want to enter in list : ")
    size = int(input())

    Data_Input = []
    for iCnt in range(0,size,1):
        print("Please Enter the Data ")
        value = int(input())
        Data_Input.append(value)

    print("Data is  : ",Data_Input)

    Data_filter = filterX(CheckEven,Data_Input)
    print("Data after filter : ",Data_filter)

    Data_Map = mapX(multipllyByTwo,Data_filter)
    print("Data after map : ",Data_Map)

    Data_reduce = reduceX(sum,Data_Map)
    print("Result after reduce is : ",Data_reduce)

if __name__ == '__main__':
    main()



# def AcceptOuput():
#     print("Enter number of element you want to enter in list : ")
#     size = int(input())
#
#     Data_Input = []
#
#     for iCnt in range(0, size, 1):
#         print("Enter values")
#         value = int(input())
#
#         Data_Input.append(value)
#
#     return Data_Input

