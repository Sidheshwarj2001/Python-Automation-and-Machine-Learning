
def Add(a,b):
    return a+b

def Sub(a,b):
    return a- b

def Calculator(Target,Value1,Value2):
    return Target(Value1,Value2)

ret = Calculator(Target = Add,Value1=10,Value2=20)
print("Addition is : ",ret)

ret = Calculator(Target = Sub,Value1=10,Value2=11)
print("Subtraction is : ",ret)