# class blueprint of object
# also known as structure



# object real world entity of class

class Car:

    # variables
    brand = 'toyota'
    wheels = 4

    # functions
    def accelerate(self):
        print("accelerate")

    def brake(self):
        print('brake')

car1 = Car()
car1.brand = "Mahindra"
print(car1.brand)
print(car1.wheels)
car1.accelerate()
car1.brake()

car2 = Car()
print(car2.brand)
print(car2.wheels)
car2.accelerate()
car2.brake()