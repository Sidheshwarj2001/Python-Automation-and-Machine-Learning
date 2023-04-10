
def Demo():
    print("Inside Demo function")

def Hello(FPTR):
    print("Inside hello function")
    FPTR()

def fun():
    print("Inside fun ")

Hello(Demo)
Hello(fun)