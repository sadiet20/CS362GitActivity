
def find_divisors(x):
	divisors = []
	div = x
	while(not div==0):
		if(x%div==0):
			divisors.append(div)
		div = div - 1
	print(divisors)

find_divisors(8)
