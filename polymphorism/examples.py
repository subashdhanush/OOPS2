class shape():
    def area(self):
        return 0
class Rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
    
s1=shape()
print(s1.area())
l1=Rectangle()
l1.area()       