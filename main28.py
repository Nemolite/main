class Cov19:
	vacin = 1
	def __init__ (self, sick):
		self.sick = sick

	def treatment(self):
		while self.sick>0:
			self.sick-=self.vacin
		
		if self.sick == 0:
			print("It is OK")

hum = Cov19(3139258) # today
hum.treatment()
