 # Normal function   / Named Function

def Add(No1,No2):
     return No1 + No2

# Lambda function / Unnamed Function : anonymous function those function how has no name
# Syntax :  lambda parameters : body

add = lambda a , b : a + b

def main():
    Ans1 = Add(10,11)
    Ans2 = add(10,11)

    print("Addition using normal function : ", Ans1)
    print("Addition using lambda function : ",Ans2)

    print("Type of Lambda function : ",type(add))

if __name__ == '__main__':
     main()