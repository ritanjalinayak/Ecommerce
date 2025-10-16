def calulate(num):
    return num




data = calulate(14)

print(data)










class Demo:

    def __init__(self,k, a, b):
        self.k = k
        self.a = a
        self.b =b

    def findBig(self):
        if self.a > self.b:
            print(self.a ," is bigger")
        else:
            print(self.b , " is bogger")


c =20
d=90

kol = Demo(c,d)

kol.findBig()

