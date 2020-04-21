class myClass:
    count = 0
    def start(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.sum = n1+n2
        myClass.count += 1
    def show(self):
    	print(self.sum)

obj1 = myClass()
obj1.start(23,32)    	
obj1.show()