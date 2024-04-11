#two types variable:

'''1. instance variable
2. class variable'''


'''
class phone():
    chargertype="C-Type"   #class variable
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
       
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charrgertype:",self.chargertype)

samsung=phone("samsung","12000","B-type")
samsung.display()

redmi=phone("Redmi","40000","C-type")
redmi.display()

#print(phone.chargertype)
'''


class car:
    def drive(self,name):
        print("hello",name,", Let's drive!")

vehicle=car()
vehicle.drive("vachu")
