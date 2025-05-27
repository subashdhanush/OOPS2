class Company():
    def __init__(self):
        self.companyName="Google"
class B(Company):
    pass

b1=B()
c1=Company()
# print(c1.companyName)        
print(b1.companyName)