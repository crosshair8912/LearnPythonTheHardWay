def add(a,b):
	print "ADDING:%d + %d" % (a,b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING:%d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING: %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING: %d / %d" % (a,b)
	if (b != 0):
		return a / b
	else:
		return "Sry cant divide by zero"

print "Let`s do some math with just functions!"

age = add (1,22)
height = subtract(200,17)
weight = multiply(20,4)
iq = divide(2000,1)

print "Age:%d, Height:%d, Weight:%d, IQ:%d" % (age,height,weight,iq)

print "Here is a pazzle!"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes: ", what,"Can you do it by hand?"