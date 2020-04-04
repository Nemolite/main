# Создание класса Vehicle
class A:  
    def vehicle_method(self):
        print("Это родительский метод из класса A")
 
# Создание класса Car, который наследует Vehicle
class B(A):  
    def car_method(self):
        print("Это метод из дочернего класса B")

obj = B()
obj.vehicle_method() 
obj.car_method()

obj1 = A()
obj1.vehicle_method()

print(obj1)