def cheese_and_crackers(cheese_count, boxes_of_craters):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_craters
	print "Man that`s enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,10)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 512491491

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(12/2+1, 7**2)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese/2,5+amount_of_crackers)