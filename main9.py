class Car:
 
    # создание атрибутов класса
    car_count = 0
 
    # создание методов класса
    def __init__(self,a):
        Car.car_count +=1
        print(Car.car_count)
        self.param = a
        print(self.param)




car_a = Car(77)  
car_b = Car(78)  
car_c = Car(79)