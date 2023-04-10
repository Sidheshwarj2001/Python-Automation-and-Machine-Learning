# Fraction datatype

class Fraction:
    # parameteristed constroctor : aya constructor which rquire input
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self): #it return only one string
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num,new_den)

def main():

    fr1 = Fraction(3,4)
    fr2 = Fraction(3,4)

    print(fr1+fr2)
    print(fr1-fr2)
    print(fr1*fr2)
    print(fr1/fr2)

if __name__ == "__main__":
    main()