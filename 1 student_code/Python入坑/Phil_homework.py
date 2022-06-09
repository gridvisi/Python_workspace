
class Car:
    def __init__(self,type,color):
        self.type = type
        self.color = color

    def drive(self):
        return (self.type,self.color)

car1 = Car('BMW','Black')
print(car1.drive())

