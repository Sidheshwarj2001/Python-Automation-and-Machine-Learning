
import Addition
import Subtraction
import Multiplication
import Division

def main():

    print("enter a first number : ")
    no1 = int(input())
    print("enter a second number : ")
    no2 = int(input())

    Addition.add(no1,no2)
    Subtraction.sub(no1,no2)
    Multiplication.mul(no1,no2)
    Division.div(no1,no2)





if __name__ =="__main__":
    main()