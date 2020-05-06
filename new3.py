def one():
	print("test one")

def two(fn):
	fn()

two(one)