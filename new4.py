def f1(fn):
	print("я f1")
	fn()

def f2(fn1):
	print("я f2")
	fn1()

@f1
f2()	