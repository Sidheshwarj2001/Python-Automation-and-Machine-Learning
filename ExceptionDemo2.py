
def main():

    try: # try block contain which  may generate error
        # this code under run pvm

        print("Enter first Number")
        No1 = int(input())

        print("Enter second number : ")
        No2 = int(input())

        Ans = No1 / No2
        print("Division is : ", Ans)

    except ZeroDivisionError: #it catch which is error
        print("Inside zero division Error")

    except ValueError:
        print("inside value error")

    except Exception: # ha shevti pahije
        # generlize catch block he block sagle error yetat Exception chya at
        print("Inside last except Block")

    finally:
        #this block run every time
        # why it write -if our code contain some resources
        print("Inside finally block")

    print("inside all block")

if __name__ == '__main__':
    main()