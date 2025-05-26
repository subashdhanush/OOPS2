class Animal():
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Bird Sings")

a1=Animal()
a1.sound()  
d1=Dog()
d1.sound()
b1=Bird()
b1.sound()
# a1=Dog()
# a1.sound()      