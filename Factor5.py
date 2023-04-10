
# import NumberFactor

# from NumberFactor import DisplayFactor

# from NumberFactor import *
# generalize import

import NumberFactor as NUM
# NUM is neekname of function


def main():

    print("Enter a number")
    no = int(input())

    # NumberFactor.DisplayFactor(no)
    NUM.DisplayFactor(no)

if __name__ == "__main__":
    main()

