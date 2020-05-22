import math

def myst(y):
	return round(math.sqrt(math.fabs(6.4*y)),3)

def myex(y,h):
	mye = 2.7182818284 # число e
	return round(math.pow(mye,(y+h)))

def funcT(h,y):
	sum = myst(y) + myex(y,h)
	return sum


h = 0
y = 0
while (h < 10)or(y < 10):
    print(funcT(h,y))
    h = h + 1
    y = y + 1


   