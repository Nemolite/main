def func3():
	print("Я сообщение функции func3") 
	#return "Я сообщение функции func3"
	
print(func3())


def func2(func3):
	func3()


def doSomethingBefore(func):
    print("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
    print(func())
 
doSomethingBefore(func3)
#выведет:
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# Да!	

