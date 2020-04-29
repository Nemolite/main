class Stat:
 
    @staticmethod
    def method():
        print ("Это класс Stat")
 
Stat.method()


class Square:
 
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b
 
print(Square.get_squares(3, 5))

#Конструктор

class Interes:
	a = 0
	def __init__(self):
		self.a = 1
		print("Объект создан")
	def __del__(self):
		print("Объект удален")


t = Interes()
print(t.a)
del(t)

class Test3:
	__pri = 22

print(Test3._Test3__pri)