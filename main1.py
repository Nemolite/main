class Test:
	def sumer(self,per1,per2):
		self.n = per1
		self.m = per2
		self.res = self.n + self.m
		return self.res

obj1 = Test();
obj1.tem2 = obj1.sumer(2,3)
print(obj1.tem2)  #сумма 5
print(obj1.n)  # значение n 2
tem1 = obj1.m
print(obj1.m) # значение m 3

print(obj1.res) #сумма 5



#
print(dir(obj1))