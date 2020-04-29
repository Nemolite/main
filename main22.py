class Basa:
	p1 = 20
	def metod(self,a):
		self.a = a
obj1 = Basa()	
obj1.metod(22)
print(obj1.a)
print(obj1.p1)


class Car:
 
    # создание методов класса
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)


# создание класса Car
class Car2:
 
    # создание методов класса
    def __str__(self):
        return "Это объект класса Car2"
 
    def start(self):
        print ("Двигатель заведен")

    def __setattr__(self, attr):
    	if attr == 'artri2':
    		print("test")
                    
 
car_a = Car2()  
print(car_a)
car_a.artri2 = 20
print(car_a.artri2)
print(dir(car_a))


